from parser.xml_parser import parse_xml_to_csv

if __name__ == "__main__":
    input_file = "input/sample_23_subscribers.xml"
    output_file = "output/result.csv"

    parse_xml_to_csv(input_file, output_file)
