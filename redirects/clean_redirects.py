def clean_redirects(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            cleaned_line = line.split()[0]  # Split the line at whitespace and take the first part
            outfile.write(cleaned_line + '\n')

if __name__ == "__main__":
    input_file = 'redirects.txt'
    output_file = 'cleaned_redirects.txt'
    clean_redirects(input_file, output_file)
