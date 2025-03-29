# IMPORT THE LIBRARIES
import os
import subprocess
import time

# FUNCTIONS:
# CHECK IF YOU PC HAS PNPM OR NPM INTALLED:
def check_pnpm():
    try:
        subprocess.run(["pnpm", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("\n✅\u00A0Found `pnpm`, using it...")
        return "pnpm"
    except subprocess.CalledProcessError:
        pass
    except FileNotFoundError:
        pass
    
    print("\n⚠️\u00A0 `pnpm` not found, using `npm` instead...")
    return "npm"

# REPO CREATOR AND VITE LAYOUT:
def repo_creator():
    repo_name = input("Enter repository name (or type 'EXIT' to cancel): ").strip()

    if repo_name.lower() == "exit":
        print("\n❌\u00A0Operation canceled.")
        return  

    if os.path.exists(repo_name):
        print("\n⚠️\u00A0Repository already exists. Try a different name.")
        return repo_creator()

    os.makedirs(repo_name)
    os.chdir(repo_name)

    package_manager = check_pnpm()

    # EXECUTE `npm create vite@latest`
    print("\n🚀\u00A0Creating Vite project...")
    subprocess.run([package_manager, "create", "vite@latest", "."], shell=True)

    # INSTALL DEPENDENCIES
    print("\n📦\u00A0Installing dependencies...")
    subprocess.run([package_manager, "install"], shell=True)

    # GIT INIT
    print("\n🔧\u00A0Initializing Git repository...")
    subprocess.run(["git", "init"], shell=True)

    # OPEN VISUAL STUDIO CODE
    print("\n🖥️\u00A0Opening Visual Studio Code...")
    subprocess.run(["code", "."], shell=True)

    # DELAY VISUAL STUDIO OPENING
    time.sleep(2)

    # OPEN TERMINAL AND EXECUTE `npm run dev` IN VISUAL STUDIO CODE
    print("\n🚀\u00A0Running development server in VS Code terminal...")
    terminal_command = f'code . --add . && cmd /c start cmd /k "{package_manager} run dev"'
    subprocess.run(terminal_command, shell=True)

    print(f"\n✅\u00A0Repository and Vite Layout created successfully!")




# FOLDERS CREATOR
def folders_creator():
    while True:
        new_folder = input("Enter new folder name (or type 'EXIT' to cancel): ").strip()

        if new_folder.lower() == "exit":
            print("\n❌\u00A0Operation canceled.")
            break 

        if os.path.exists(new_folder):
            print("\n⚠️ \u00A0Folder already exists. Try a different name.")
        else:
            os.makedirs(new_folder)
            print(f"\n✅\u00A0Folder '{new_folder}' created!")
            break 


# FOLDERS NAVIGATION
def folders_navigation():
    while True:
        # GET ACTUAL DIRECCION AND LIST THE FOLDERS
        current_path = os.getcwd()
        folders = [f for f in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, f))]

        # CREATE THREE NEW OPTIONS
        folders.append("CREATE A NEW FOLDER")
        folders.append("CREATE A NEW REPOSITORY")
        folders.append("EXIT")

        print(f"\n📂\u00A0Current directory: {current_path}\n")
        for idx, folder in enumerate(folders, 1):
            print(f"{idx}. {folder}")

        # USER CHOOSE
        try:
            user_choice = int(input("\nSELECT A NUMBER OF YOUR CHOICE: "))
            if user_choice < 1 or user_choice > len(folders):
                print("\n❌\u00A0Invalid choice, try again.")
                continue  
        except ValueError:
            print("\n❌\u00A0Please enter a valid number.")
            continue 

        # GET THE OPTION OF THE USER
        selected_folder = folders[user_choice - 1]

        if selected_folder == "EXIT":
            print("\n👋\u00A0Exiting...")
            break  

        elif selected_folder == "CREATE A NEW FOLDER":
            folders_creator()

        elif selected_folder == "CREATE A NEW REPOSITORY":
            repo_creator()

        else:
            os.chdir(os.path.join(current_path, selected_folder))
            print(f"\n📂\u00A0Entered '{selected_folder}'")


# ORIGIN - STEP 1: GET THE REPOS MAIN FOLDER AND EXECUTE ALL FUNCTIONS ABOVE 
repo_routes = r"C:\A_Proyects"
os.chdir(repo_routes)
folders_navigation()
