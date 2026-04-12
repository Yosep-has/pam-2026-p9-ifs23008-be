# 1. Pastikan Python sudah terinstall

```bash
python --version
```

# 2. Buat virtual environment

```bash
python -m venv venv --without-pip
```

# 3. Aktifkan virtual environment

```bash
# CMD
venv\Scripts\activate

# POWERSHELL
.\venv\Scripts\activate

# Install pip
python -m ensurepip --upgrade
```

# 4. Install Library

```bash
pip install -r requirements.txt
```

# 4. Run
```bash
python app.py
```