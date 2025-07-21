from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="student-management-system",
    version="0.1.0",
    packages=find_packages(include=["app", "app.*"]),  # Adjust 'app' if needed
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.6",  # Adjust based on your lowest Python target
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

