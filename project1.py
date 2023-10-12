def main():
    condense_page_name("   Ball State University    ")
    

def condense_page_name(page_name: str):
    condensed_page_name = page_name.strip()
    condensed_page_name = condensed_page_name.replace(" ", "_")
    return condensed_page_name


if __name__ == "__main__":
    main()