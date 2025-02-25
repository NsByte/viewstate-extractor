import re
import argparse

def extract_viewstate(file_path, verbose=False):
    # Define the regex pattern
    pattern = re.compile(
        r'<input\s+type="hidden"\s+name="(__VIEWSTATEGENERATOR|__VIEWSTATE)"\s+id="[^"]*"\s+value="([^"]*)"[^>]*>'
    )

    try:
        # Read the file content
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Find all matches
        matches = pattern.findall(html_content)

        if matches:
            # Initialize a list to hold the current group of states
            current_group = []
            current_viewstategenerator = None

            # Loop through each match
            for match in matches:
                # If it's a __VIEWSTATE
                if match[0] == "__VIEWSTATE":
                    if current_group:
                        # Print the current group of states and reset it
                        if verbose:
                            print(f"__VIEWSTATE: {current_group[0][1]}")
                            print(f"__VIEWSTATEGENERATOR: {current_viewstategenerator}")
                        else:
                            print(current_group[0][1])
                            print(current_viewstategenerator)
                    
                    # Reset current group for the new __VIEWSTATE
                    current_group = [(match[0], match[1])]
                    current_viewstategenerator = None  # Reset the generator for the new group
                else:  # It's a __VIEWSTATEGENERATOR
                    if not current_viewstategenerator:
                        current_viewstategenerator = match[1]

            # After the loop, print the last group if it exists
            if current_group:
                if verbose:
                    print(f"__VIEWSTATE: {current_group[0][1]}")
                    print(f"__VIEWSTATEGENERATOR: {current_viewstategenerator}")
                else:
                    print(current_group[0][1])
                    print(current_viewstategenerator)
            
        else:
            print("\nNo __VIEWSTATE or __VIEWSTATEGENERATOR found.")

    except FileNotFoundError:
        print("\nError: File not found!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# Command-line argument support
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract __VIEWSTATE and __VIEWSTATEGENERATOR from an HTML file.")
    parser.add_argument("file", help="Path to the HTML file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed __VIEWSTATE and __VIEWSTATEGENERATOR values")
    args = parser.parse_args()

    extract_viewstate(args.file, verbose=args.verbose)
