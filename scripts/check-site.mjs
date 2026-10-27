import { readdir, readFile, stat } from 'node:fs/promises';
import path from 'node:path';

const root = path.resolve('dist');
const origin = 'https://huziidroid.github.io';
const base = '/agentfabric-docs';
const failures = [];
const anchorCache = new Map();

async function files(directory) {
  const result = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const name = path.join(directory, entry.name);
    if (entry.isDirectory()) result.push(...await files(name));
    else if (name.endsWith('.html')) result.push(name);
  }
  return result;
}
function decode(value) {
  return value.replace(/&amp;/g, '&').replace(/&#(\d+);/g, (_, code) => String.fromCodePoint(Number(code)));
}
async function exists(file) {
  try { return await stat(file); } catch { return undefined; }
}
const pages = await files(root);
let checked = 0;
for (const page of pages) {
  const relative = path.relative(root, page).split(path.sep).join('/');
  const pageUrl = new URL(`${base}/${relative.replace(/index\.html$/, '')}`, origin);
  const html = await readFile(page, 'utf8');
  for (const match of html.matchAll(/\b(href|src)="([^"]*)"/g)) {
    const value = decode(match[2]);
    if (!value || /^(data:|mailto:|tel:|javascript:)/.test(value)) continue;
    let url;
    try { url = new URL(value, pageUrl); } catch { failures.push(`${relative}: invalid URL ${value}`); continue; }
    if (url.origin !== origin) continue;
    if (url.pathname !== base && !url.pathname.startsWith(`${base}/`)) {
      failures.push(`${relative}: URL escapes Pages base: ${value}`);
      continue;
    }
    let target = path.join(root, decodeURIComponent(url.pathname.slice(base.length)));
    const info = await exists(target);
    if (info?.isDirectory()) target = path.join(target, 'index.html');
    if (!await exists(target)) {
      failures.push(`${relative}: missing target ${value}`);
      continue;
    }
    checked++;
    if (match[1] === 'href' && url.hash && target.endsWith('.html')) {
      if (!anchorCache.has(target)) {
        const content = await readFile(target, 'utf8');
        anchorCache.set(target, new Set([...content.matchAll(/\b(?:id|name)="([^"]+)"/g)].map(item => decode(item[1]))));
      }
      const anchor = decodeURIComponent(url.hash.slice(1));
      if (!anchorCache.get(target).has(anchor)) failures.push(`${relative}: missing anchor ${value}`);
    }
  }
}
if (!await exists(path.join(root, 'pagefind/pagefind.js'))) failures.push('Missing production search index.');
if (failures.length) {
  console.error([...new Set(failures)].join('\n'));
  process.exitCode = 1;
} else {
  console.log(`Verified ${pages.length} HTML pages, ${checked} internal links/assets, fragment targets, and production search assets.`);
}
