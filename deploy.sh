#!/bin/bash

echo "🚀 Déploiement UPF – démarrage"

# Aller dans le dossier du projet
cd /var/www/upf-asso.fr/upf_asso || exit

echo "📥 Pull Git..."
git pull

echo "📦 Collectstatic..."
source venv/bin/activate
python manage.py collectstatic --noinput

echo "🔄 Migration..."
python manage.py migrate --noinput

echo "🔥 Redémarrage Gunicorn..."
systemctl restart gunicorn-upf.service

echo "🌐 Reload Nginx..."
systemctl reload nginx

echo "✅ Déploiement terminé avec succès"