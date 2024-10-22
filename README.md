# Installation

## Pelican and other dependencies
```bash
pip install -r requirements.txt
```

## Ameising theme
```bash
pelican-themes --install themes/ameising-site --verbose
```

## Tailwind / DaisyUI
```bash
npm install -D tailwindcss
npx tailwindcss init
npm i -D daisyui@latest
```


# Develop / build

## Tailwind / DaisyUI
```bash
npx tailwindcss -i ./themes/ameising-site/input.css -o ./themes/ameising-site/static/css/ameising.css --watch
```

## Pelican
```bash
pelican -r -l
```

## Update theme
```bash
pelican-themes --upgrade themes/ameising-site --verbose
```

