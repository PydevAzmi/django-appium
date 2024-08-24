from appium import webdriver
import subprocess
import base64
import time
from appium.options.common.base import AppiumOptions
from selenium.webdriver.common.by import By

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Define the desired capabilities for the Android emulator
capabilities = dict(
        platformName='Android',
        platformVersion="10.0",
        automationName='uiautomator2',
        deviceName='Small_Phone',
        app="C:/Users/3AzMii/Downloads/ApiDemos-debug.apk",
        language='fr',
        locale='FR'
        )

# Start the Android emulator using a command (adjust according to your setup)
print("Starting adb server and Android Emulator ...")
subprocess.Popen(["emulator", "-avd", "Small_Phone"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the emulator to fully start
time.sleep(10)
print("adb server and Android Emulator Started well...")
print("------------------------------------------------")


# Start the Appium session
print("Starting the Appium session ...")
driver = webdriver.Remote("http://localhost:4723/wd/hub",  options=AppiumOptions().load_capabilities(capabilities))

# Wait for the app to launch
time.sleep(10)
print("Starting the Appium session Started well...")
print("------------------------------------------------")

# Start recording video
driver.start_recording_screen()

# Start recording video
driver.start_recording_screen()

# Capture the UI elements hierarchy
initial_ui_hierarchy = driver.page_source

# Save the hierarchy to an XML file
with open("initial_ui_hierarchy.xml", "w", encoding="utf-8") as file:
    file.write(initial_ui_hierarchy)
print("Initial UI hierarchy captured.")
print("------------------------------------------------")



# Take a screenshot of the initial screen
initial_screenshot_path = "initial_screen.png"
driver.save_screenshot(initial_screenshot_path)
print(f"Initial screen screenshot saved at {initial_screenshot_path}")
print("------------------------------------------------")

# Simulate a click on the first button
print("Simulate a click on the first button ...")
# Example of a tap action using W3C actions
actions = ActionChains(driver)
pointer = PointerInput('touch', 'finger')
element = driver.find_element(By.XPATH, "//android.widget.TextView[@text='Accessibility']")
actions.move_to_element(element).click()
actions.perform()
time.sleep(3)  # Wait for the screen to change
print("------------------------------------------------")

# Assess whether the screen changed by comparing the UI hierarchies
new_ui_hierarchy = driver.page_source
screen_changed = initial_ui_hierarchy != new_ui_hierarchy
print(f"Screen change detected: {screen_changed}")
print("------------------------------------------------")

# Save the hierarchy to an XML file
with open("new_ui_hierarchy.xml", "w", encoding="utf-8") as file:
    file.write(new_ui_hierarchy)
print("New UI hierarchy captured.")
print("------------------------------------------------")

# Take a screenshot of the subsequent screen
subsequent_screenshot_path = "subsequent_screen.png"
driver.save_screenshot(subsequent_screenshot_path)
print(f"Subsequent screen screenshot saved at {subsequent_screenshot_path}")
print("------------------------------------------------")


# Perform more actions or wait for video recording
time.sleep(10)

# Stop recording and save the video
video_data = driver.stop_recording_screen()
# If video_data is a base64 encoded string
video_data = base64.b64decode(video_data)
with open("recorded_video.mp4", "wb") as video_file:
    video_file.write(video_data)

print(f"Test recording saved successfully.")
print("------------------------------------------------")

# Close the Appium session
driver.quit()

# Stop the Android emulator
subprocess.Popen(["adb", "-s", "emulator-5554", "emu", "kill"])

print(f"Test sompleted successfully.")
