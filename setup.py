# import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kwik",
    version="0.0.1",
    description="kwik framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sroedger/kwik",
    author="Sam Roedger",
    author_email="sroedger@gmail.com",
    license="MIT",
    install_requires=[],
    extra_require={"dev": []},
    keywords=[
        "kwik",
        "framework",
        "kwik framework",
        "web",
        "web development",
        "services",
        "microservices",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
