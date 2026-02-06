@echo off
echo ========================================
echo   Sentinel AI - Quick Start
echo ========================================
echo.

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not running!
    echo Please start Docker Desktop and try again.
    pause
    exit /b 1
)

echo [OK] Docker is running
echo.

REM Check if .env exists
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env >nul
    echo [OK] .env file created
    echo.
    echo IMPORTANT: Edit .env and add your GEMINI_API_KEY if you have one
    echo Press any key to continue...
    pause >nul
)

echo Starting Sentinel AI...
echo.
echo This will:
echo   1. Build Docker containers
echo   2. Start all services
echo   3. Open the app in your browser
echo.

docker compose up --build -d

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to start services
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Sentinel AI is running!
echo ========================================
echo.
echo   Frontend:  http://localhost:3000
echo   Backend:   http://localhost:8000
echo   API Docs:  http://localhost:8000/docs
echo.
echo Opening in browser...
timeout /t 3 >nul
start http://localhost:3000

echo.
echo Press any key to view logs (Ctrl+C to exit logs)
pause >nul
docker compose logs -f
