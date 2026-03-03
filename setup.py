import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_descrition = f.read()

__version__ ="0.0.0"

REPO_NAME = "FoodDelivery-Crisis-Analysis"
AUTHOR_USER_NAME = "Vandan"
SRC_REPO = "fdca"
AUTHOR_EMAIL = "iamvandanprajapati@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A analysis of Crisis on Food Delivery",
    long_description=long_descrition,
    url=f"https://github.com/vandanvlog/FoodDelivery-Crisis-Analysis",
    project_urls={
        "FoodDelivery-Crisis-Analysis": f"https://github.com/vandanvlog/FoodDelivery-Crisis-Analysis"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
