#Create the basic script
git add temperature_converter.py
git commit -m "Add temperature converter script"
#add celsius to Farenhite converter
git add temperature_converter.py
git commit -m "Add Celsius to Fahrenheit conversion"
#Add Farenhite to celsius conversion
git add temperature_converter.py
git commit -m "Add Fahrenheit to Celsius conversion"
#complete workflow 
mkdir temperature-converter
cd temperature-converter

git init

# Create temperature_converter.py and add your code

git add .
git commit -m "Add temperature converter script"

# Make your second change
git add .
git commit -m "Add Celsius to Fahrenheit conversion"

# Make your third change
git add .
git commit -m "Add Fahrenheit to Celsius conversion"

git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
