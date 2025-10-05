from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Setup Chrome Driver
service = Service("C:\\Users\\mkamr\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Eduko Courses page
driver.get("https://eduko.spikotech.com/Course")

# Wait for all course cards to load
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'card-body text-center')]"))
)

# Find all course containers
product_cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'card-body text-center')]")

# Lists to store data
names, descriptions,codes,instructors,semesters = [], [],[],[],[]
#lists to stores clos
clo1,clo2,clo3,clo4=[],[],[],[]
#lists to store books
book1,book2=[],[]

# Loop through each course card
for i, card in enumerate(product_cards):
    #get course name
    
    try:
        name = card.find_element(By.XPATH, ".//h4").text
    except:
        name = "N/A"

    #get course link for navigating
    try:
        link = card.find_element(By.XPATH, ".//a").get_attribute("href")
    except:
        link = None
        
    #get course instructor
    try:
        instructor=card.find_element(By.XPATH,".//h7[1]").text
    except:
        instructor="NA"
        
    #get semester
    try:
        sems=card.find_element(By.XPATH,".//h7[2]").text
    except:
        sems="NA"

    
    # Open course link in new tab
    if link:
        driver.execute_script("window.open(arguments[0]);", link)
        driver.switch_to.window(driver.window_handles[-1])

        try:
            # Wait for course description to load
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            time.sleep(2)
            
            # Get the text of the description
            desc_text = driver.find_element(By.XPATH, ".//p[contains(@id,'CourseDescription')]").text
        except:
            desc_text = "No description found"
            
        #get course code 
        try:
            coursecode=driver.find_element(By.XPATH,".//div[contains(@id,'CourseCode')]").text
        except:
            coursecode="NA"
            
        #get clos
        clo1_text, clo2_text, clo3_text, clo4_text = "N/A", "N/A", "N/A", "N/A"
        try:
            clos=driver.find_elements(By.XPATH, ".//ul[@id='CourseClos']/li")
            clos_text = [clo.text.strip() for clo in clos if clo.text.strip() != ""]
            # Assign to clo1–clo4 safely
            if len(clos_text) > 0: clo1_text = clos_text[0]
            if len(clos_text) > 1: clo2_text = clos_text[1]
            if len(clos_text) > 2: clo3_text = clos_text[2]
            if len(clos_text) > 3: clo4_text = clos_text[3]
        except:
            pass
        
        
        #get clos
        book_text,book2_text = "N/A", "N/A"
        try:
            books=driver.find_elements(By.XPATH, ".//ul[@id='CourseBooks']/li")
            books_text = [book.text.strip() for book in books if book.text.strip() != ""]
            # Assign to clo1–clo4 safely
            if len(books_text) > 0: book_text = books_text[0]
            if len(books_text) > 1: book2_text = books_text[1]
        except:
            pass
            
            
        # Close this tab and go back to the main one
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)  # small delay for stability

    names.append(name)
    descriptions.append(desc_text)
    codes.append(coursecode)
    instructors.append(instructor)
    clo1.append(clo1_text)
    clo2.append(clo2_text)
    clo3.append(clo3_text)
    clo4.append(clo4_text)
    book1.append(book_text)
    book2.append(book2_text)
    semesters.append(sems)

# Save data to CSV
df = pd.DataFrame({ 
    "Course Code":codes,
    "Title": names,
    "Description": descriptions,
    "CLO1":clo1,
    "CLO2":clo2,
    "CLO3":clo3,
    "CLO4":clo4,
    "TextBook1":book1,
    "TextBook2":book2,
    "instructor":instructors,
    "Semester":semesters
})

df.to_csv("eduko_courses.csv", index=False, encoding="utf-8")
print("✅ Done — Data saved to eduko_courses.csv")

driver.quit()

