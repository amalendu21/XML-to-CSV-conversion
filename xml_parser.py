from lxml import etree
import pandas as pd

def parse_xml_to_csv(xml_file, csv_output):

    records = []

    context = etree.iterparse(xml_file, events=("end",), tag="Subscriber")

    for event, elem in context:
        details = elem.find("SubscriberDetails")
        service = elem.find("ServiceProfile")

        record = {
            "MSISDN": details.findtext("MSISDN"),
            "IMSI": details.findtext("IMSI"),
            "ICCID": details.findtext("ICCID"),
            "CustomerCategory": details.findtext("CustomerCategory"),
            "Circle": details.findtext("Circle"),
            "PlanID": service.findtext("PlanID"),
            "DataQuotaGB": service.findtext("DataQuotaGB"),
            "ValidityDays": service.findtext("ValidityDays"),
        }

        records.append(record)
        elem.clear()

    df = pd.DataFrame(records)
    df.to_csv(csv_output, index=False)

    print(f"Converted {len(records)} subscribers successfully.")
