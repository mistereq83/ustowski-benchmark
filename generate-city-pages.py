#!/usr/bin/env python3
"""
Generate city-specific SEO pages from template + data.
Usage: python3 generate-city-pages.py [--dry-run]
"""
import json
import sys
import os

TEMPLATE = 'src/_template-city.html'
DATA = 'city-data.json'
OUT_DIR = 'src'

def generate_related_links(service_slug, current_city_slug, cities):
    links = []
    for cslug, cdata in cities.items():
        if cslug == current_city_slug:
            links.append(f'<span class="px-4 py-2 bg-accent text-white rounded-full text-sm font-medium">{cdata["name"]}</span>')
        else:
            links.append(f'<a href="{service_slug}-{cslug}.html" class="px-4 py-2 bg-secondary hover:bg-accent hover:text-white rounded-full text-sm font-medium transition-colors">{cdata["name"]}</a>')
    return '\n                '.join(links)

def generate_page(template, city, service, all_cities):
    cs = city['slug']
    ss = service['page'].replace('.html', '')
    filename = f'{ss}-{cs}.html'
    intro = service['intro_templates'][cs]
    challenges = city['challenges']
    
    replacements = {
        '{{FILENAME}}': filename,
        '{{TITLE}}': f'{service["name"]} {city["name"]}',
        '{{META_DESC}}': f'{service["name"]} w {city["locative"]} — profesjonalne usługi firmy Ustowski. Ceny od {service["price_range"]} {service["price_unit"]}. Bezpłatna wycena. Tel. 663 719 372.',
        '{{HERO_IMG}}': service['hero_img'],
        '{{SERVICE_NAME}}': service['name'],
        '{{SERVICE_NAME_SHORT}}': service['name_short'],
        '{{SERVICE_NAME_GENITIVE}}': service['name_genitive'],
        '{{SERVICE_PAGE}}': service['page'],
        '{{CITY}}': city['name'],
        '{{CITY_LOCATIVE}}': city['locative'],
        '{{CITY_GENITIVE}}': city['genitive'],
        '{{H1}}': f'{service["name"]} {city["name"]}',
        '{{HERO_DESC}}': f'Profesjonalne {service["name_short"]} w {city["locative"]} i okolicach. Sprzęt przemysłowy, doświadczony zespół, gwarancja jakości.',
        '{{INTRO_HEADLINE}}': intro['headline'],
        '{{INTRO_P1}}': intro['p1'],
        '{{INTRO_P2}}': intro['p2'],
        '{{INTRO_P3}}': intro['p3'],
        '{{CHALLENGES_INTRO}}': city['characteristics']['problems'],
        '{{CHALLENGE_1_ICON}}': challenges['1']['icon'],
        '{{CHALLENGE_1_TITLE}}': challenges['1']['title'],
        '{{CHALLENGE_1_DESC}}': challenges['1']['desc'],
        '{{CHALLENGE_2_ICON}}': challenges['2']['icon'],
        '{{CHALLENGE_2_TITLE}}': challenges['2']['title'],
        '{{CHALLENGE_2_DESC}}': challenges['2']['desc'],
        '{{CHALLENGE_3_ICON}}': challenges['3']['icon'],
        '{{CHALLENGE_3_TITLE}}': challenges['3']['title'],
        '{{CHALLENGE_3_DESC}}': challenges['3']['desc'],
        '{{SERVICE_ID}}': ss,
        '{{PRICE_RANGE}}': service['price_range'],
        '{{PRICE_UNIT}}': service['price_unit'],
        '{{PRICE_NOTE}}': service['price_note'],
        '{{DISTANCE}}': city['distance'],
        '{{DRIVE_TIME}}': city['drive_time'],
        '{{PROCESS_STEP3}}': service['process_step3'],
        '{{RELATED_CITIES_LINKS}}': generate_related_links(ss, cs, all_cities),
    }
    
    result = template
    for key, value in replacements.items():
        result = result.replace(key, value)
    
    return result

def main():
    dry_run = '--dry-run' in sys.argv
    
    with open(TEMPLATE, 'r') as f:
        template = f.read()
    
    with open(DATA, 'r') as f:
        data = json.load(f)
    
    cities = data['cities']
    services = data['services']
    
    generated = 0
    for service_slug, service in services.items():
        for city_slug, city in cities.items():
            filename = f'{service_slug}-{city_slug}.html'
            filepath = os.path.join(OUT_DIR, filename)
            
            page = generate_page(template, city, service, cities)
            
            # Check for unreplaced placeholders
            import re
            unreplaced = re.findall(r'\{\{[A-Z_]+\}\}', page)
            if unreplaced:
                print(f'  ⚠️  {filename}: unreplaced: {unreplaced}')
            
            if dry_run:
                print(f'  [DRY] {filename} ({len(page)} bytes)')
            else:
                with open(filepath, 'w') as f:
                    f.write(page)
                print(f'  ✅ {filename} ({len(page)} bytes)')
            
            generated += 1
    
    print(f'\n{"[DRY RUN] " if dry_run else ""}Generated {generated} city pages.')

if __name__ == '__main__':
    main()
