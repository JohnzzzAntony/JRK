# 🚀 Vercel Deployment Guide for JKR

I've updated your project to be production-ready for Vercel. Since Vercel is serverless, we've switched your storage to **Cloudinary** for media and **WhiteNoise** for static files.

## ✅ Changes Made
1.  **`requirements.txt`**: Updated with modern versions and added `psycopg2-binary`, `whitenoise`, and `dj-database-url`.
2.  **`jkr/wsgi.py`**: Added `app = application` for Vercel compatibility.
3.  **`jkr/settings.py`**: 
    -   Configured **WhiteNoise** to handle static files.
    -   Configured **Cloudinary** as the default media storage (Vercel doesn't have persistent storage for local `/media/`).
    -   Added `.vercel.app` to `ALLOWED_HOSTS`.

---

## 🛠️ Deployment Steps

### 1. Database (CRITICAL)
Vercel is stateless. You **cannot** use the local `db.sqlite3` file on Vercel (it will reset every time the server restarts).
1.  Go to the **Storage** tab in your Vercel Dashboard.
2.  Create a new **Vercel Postgres** database.
3.  Follow the instructions to connect it to your project. This will automatically add `POSTGRES_URL` to your environment variables.

### 2. Environment Variables
In your Vercel Project Settings > Environment Variables, add the following (copy from your `.env`):
-   `SECRET_KEY` (Generate a new secure one for production)
-   `DEBUG`= `False`
-   `STRIPE_SECRET_KEY` & `STRIPE_PUBLISHABLE_KEY`
-   `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`
-   `EMAIL_HOST_USER` & `EMAIL_HOST_PASSWORD`
-   `DATABASE_URL` (Map this to your `POSTGRES_URL` provided by Vercel)

### 3. Static Files
Vercel needs your static files to be collected. 
**Run this locally before pushing your code:**
```bash
python manage.py collectstatic --noinput
```
*Wait: I've configured WhiteNoise to handle this, but if your deployment fails, make sure the `staticfiles` folder is pushed to GitHub or use a build command.*

### 4. Push to GitHub
1.  Commit your changes:
    ```bash
    git add .
    git commit -m "Configure for Vercel deployment"
    git push origin main
    ```
2.  Connect your GitHub repo to Vercel.
3.  Deploy!

---

## ⚡ Important Notes
-   **Migrations**: Since Vercel is serverless, you can't run `python manage.py migrate` directly in a terminal like on a standard server. You should run it as a **Build Step** or use a temporary "migrator" route.
    -   *Easiest way:* Connect to your data via local terminal and run `python manage.py migrate` pointing to the Vercel Postgres URL.
-   **Admin Access**: Ensure you create a superuser on the new Postgres database once live.
