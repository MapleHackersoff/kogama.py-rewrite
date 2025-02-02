import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KoGaMa.py-Rewrite",
    packages = ['Kogama'],
    version="0.4",
    author="TheNoobPro44",
    author_email="TheNewbiePro44@gmail.com",
    description="KoGaMa.py-Rewrite is a API-wrapper for KoGaMa.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheNoobPro44/KoGaMa.py-Rewrite/",
    project_urls={
        "Bug Tracker": "https://github.com/TheNoobPro44/KoGaMa.py-Rewrite/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
