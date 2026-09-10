# 🚀 1-CLICK GITHUB PUSH SCRIPT
# Run this script in PowerShell from your project directory to instantly push to GitHub Codespaces!

Param(
    [Parameter(Mandatory=$true)]
    [string]$GitHubRepoUrl
)

Write-Host "📦 Step 1: Initializing Workspace Structure..." -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path "./workspace" | Out-Null
New-Item -ItemType Directory -Force -Path "./.devcontainer" | Out-Null

Write-Host "📄 Step 2: Preparing AGENTS.md & Configurations..." -ForegroundColor Cyan
Get-Content "C:\Users\tanji\.gemini\antigravity\brain\0b27dd24-7b8d-4862-8f4d-b5ce227a980e\universal_execution_kit.md" | Out-File -FilePath "./workspace/README_KIT.md" -Encoding utf8
Get-Content "C:\Users\tanji\.gemini\antigravity\brain\0b27dd24-7b8d-4862-8f4d-b5ce227a980e\master_execution_blueprint.md" | Out-File -FilePath "./master_execution_blueprint.md" -Encoding utf8
Get-Content "C:\Users\tanji\.gemini\antigravity\brain\0b27dd24-7b8d-4862-8f4d-b5ce227a980e\.devcontainer\devcontainer.json" | Out-File -FilePath "./.devcontainer/devcontainer.json" -Encoding utf8

Write-Host "🔗 Step 3: Git Initializing & Pushing to GitHub..." -ForegroundColor Cyan
git init
git add .
git commit -m "feat: initial 15-Engine Omni AI Codespaces Environment"
git branch -M main
git remote add origin $GitHubRepoUrl
git push -u origin main --force

Write-Host "✅ SUCCESS! Repository pushed to GitHub." -ForegroundColor Green
Write-Host "🌐 Next Step: Open your GitHub Repo -> Click 'Code' -> Click 'Open with Codespaces'." -ForegroundColor Yellow
