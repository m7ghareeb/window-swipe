#!/usr/bin/env python3
# Checks metadata.json, settings-schema.json and CHANGELOG.md for release consistency:
# required/forbidden fields and ASCII (Cinnamon Spices rules), a MAJOR.MINOR.PATCH version that
# matches the newest CHANGELOG entry, and settings defaults that exist among their options.
import json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
UUID = 'window-swipe@ghareeb'
errors = []

meta = json.load(open(os.path.join(ROOT, UUID, 'metadata.json'), encoding='utf-8'))
for field in ('uuid', 'name', 'description', 'version', 'author', 'cinnamon-version'):
    if field not in meta:
        errors.append(f'metadata.json: missing "{field}"')
for field in ('icon', 'dangerous', 'last-edited'):
    if field in meta:
        errors.append(f'metadata.json: forbidden field "{field}"')
if meta.get('uuid') != UUID:
    errors.append('metadata.json: uuid does not match the folder name')
for key, value in meta.items():
    if not str(value).isascii():
        errors.append(f'metadata.json: non-ASCII characters in "{key}"')
version = meta.get('version', '')
if not re.fullmatch(r'\d+\.\d+\.\d+', version):
    errors.append(f'metadata.json: version "{version}" is not MAJOR.MINOR.PATCH')

changelog = open(os.path.join(ROOT, 'CHANGELOG.md'), encoding='utf-8').read()
released = re.findall(r'^## \[(\d+\.\d+\.\d+)\]', changelog, re.M)
if not released or released[0] != version:
    errors.append(f'CHANGELOG.md: newest release is {released[:1]}, metadata.json says {version}')

schema = json.load(open(os.path.join(ROOT, UUID, 'settings-schema.json'), encoding='utf-8'))
for key, setting in schema.items():
    if setting.get('type') == 'combobox' and setting['default'] not in setting['options'].values():
        errors.append(f'settings-schema.json: default of "{key}" is not one of its options')

info = json.load(open(os.path.join(ROOT, 'spices', 'info.json'), encoding='utf-8'))
if not info.get('author'):
    errors.append('spices/info.json: missing "author"')

for e in errors:
    print('ERROR:', e)
print(f'checked {UUID} {version}: {"OK" if not errors else f"{len(errors)} error(s)"}')
sys.exit(1 if errors else 0)
