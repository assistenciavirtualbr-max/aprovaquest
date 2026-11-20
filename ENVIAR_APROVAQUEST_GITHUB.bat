@echo off
chcp 65001 > nul
title Publicando AprovaQuest no GitHub (PWA e Vendas)
cd /d "%~dp0"
echo ======================================================================
echo       PUBLICANDO APROVAQUEST NO GITHUB (PWA + VENDA ATIVA)
echo ======================================================================
echo.
echo Repositório configurado:
echo https://github.com/assistenciavirtualbr-max/aprovaquest.git
echo.
echo [*] Verificando configuração do Git...

git remote get-url origin >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [*] Conectando ao repositório remoto do GitHub...
    git remote add origin https://github.com/assistenciavirtualbr-max/aprovaquest.git
)

echo [*] Adicionando e salvando arquivos atualizados...
git add .
git commit -m "feat: PWA para celular (Android/iOS), pagina de vendas e ativacao VIP"

echo.
echo [*] Enviando arquivos para o GitHub...
echo (Se abrir uma janela do navegador, clique em "Sign in with your browser" ou "Authorize")
echo.
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================================
    echo  🎉 PARABÉNS! PROJETO ENVIADO COM SUCESSO PARA O GITHUB!
    echo ======================================================================
    echo.
    echo Para ativar o link online definitivo e gratuito para seus clientes:
    echo 1. Acesse: https://github.com/assistenciavirtualbr-max/aprovaquest/settings/pages
    echo 2. Em "Build and deployment" - "Branch", escolha "main" e pasta "/ (root)".
    echo 3. Clique em "Save".
    echo.
    echo Em instantes o seu aplicativo estará no ar em:
    echo 📲 https://assistenciavirtualbr-max.github.io/aprovaquest/
    echo.
    echo E a página de vendas em:
    echo 💰 https://assistenciavirtualbr-max.github.io/aprovaquest/landing-vendas.html
    echo.
) else (
    echo.
    echo [!] Se ocorrer erro de autenticação ou se o repositório ainda não foi criado:
    echo 1. Acesse: https://github.com/new
    echo 2. Nome do repositório: aprovaquest
    echo 3. Marque "Public" e clique em "Create repository" (sem marcar README).
    echo 4. Depois execute este arquivo novamente!
    echo.
)

pause
