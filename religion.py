import pandas as pd
import os
import random
import re
import hextorgb




def familyGen(input_file_path, output_folder_path):

    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(input_file_path, sheet_name="religion")

    # Create a folder to store the text files
    folder_path = output_folder_path
    os.makedirs(folder_path, exist_ok=True)

    # Loop through the rows of the DataFrame
    for index, row in df.iterrows():
        name = row["name"]
        first_word = name.split(" ")[0].lower()  # Convert first_word to lowercase
        mainFamName = re.sub(r'\W+', '', name).lower()
        print (mainFamName)
        value = row["origin"]

        # Check if the value in column i is 0
        if value == 0:
            # Write the name to a text file with "00_" at the start
            file_name = f"00_{mainFamName}.txt"
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"rf_{mainFamName} = {{\n\tgraphical_faith = 'orthodox_gfx' \n\thostility_doctrine = abrahamic_hostility_doctrine\n\tdoctrine_background_icon = core_tenet_banner_christian.dds\n}}")


def religionChildren(input_file_path, output_file_path):
    def find_children(df):
        children = {}
        for index, row in df.iterrows():
            parent = row["origin"]
            child = row["i"]
            if parent in children:
                children[parent].append(child)
            else:
                children[parent] = [child]
        df["children"] = df["i"].map(children).apply(lambda x: x if x is not None else [])
        return df

    file_path = input_file_path
    df = pd.read_excel(file_path, sheet_name="religion")

    # Call the function
    result = find_children(df)
    result.to_excel(output_file_path, index=False)

    # Print the result
    print(result)


def relGenChil(input_file_path, output_file_path):
    # Read the Excel file
    df = pd.read_excel(input_file_path)

    # Create an empty list of lists to store the values of "cName"
    cName = [[] for _ in range(len(df))]

    # Loop through each row
    for index, row in df.iterrows():
        # Check if the "children" column value is a string
        if isinstance(row['children'], str):
            # Get the "children" column value as a list of integers
            children = [int(x) for x in row['children'][1:-1].split(',')]

            # Loop through each child_id number in the list
            for child_id in children:
                # Find the matching "i" value in the "i" column
                match = df.loc[df['i'] == child_id]

                # Append the value in the "name" column to the "cName" list for the current row
                cName[index].append(match.iloc[0]['name'])

    # Add the "cName" list as a new column to the dataframe
    df['cName'] = cName

    # Save the updated dataframe to a new Excel file
    df.to_excel(output_file_path, index=False)

def religionGen(input_file_path,folder_path):
    # Load the Excel file into a pandas DataFrame
    # file_path = "combined_data.xlsx"
    # df = pd.read_excel(file_path, sheet_name="religion")

    # Load the Excel file into a pandas DataFrame
    file_path = input_file_path
    df = pd.read_excel(file_path)

    # Create a folder to store the text files
    folder_path = folder_path
    os.makedirs(folder_path, exist_ok=True)


    def color_generator():
        red = random.uniform(0, 1)
        green = random.uniform(0, 1)
        blue = random.uniform(0, 1)
        return f"{{ {red:.2f} {green:.2f} {blue:.2f} }}"


    # Loop through the rows of the DataFrame
    for index, row in df.iterrows():
        id = row["i"]
        name = row["name"]
        type = row["type"]
        first_word = name.split(" ")[0]
        value = row["origin"]
        reform = ["unreformed_faith_doctrine"]
        #paganroots = "no"

        if type == "Folk":
            paganroots = "yes"
        else:
            paganroots = "no"

    # Loop through the rows of the DataFrame
    for index, row in df.iterrows():
        id = row["i"]
        name = row["name"]
        type = row["type"]
        first_word = name.split(" ")[0]
        mainRelName = name.replace(" ", "_")
        mainFamName = re.sub(r'\W+', '', name).lower()
        print(mainFamName)
        value = row["origin"]
        reform = ["unreformed_faith_doctrine"]
        #paganroots = "no"
        children = row["cName"]
        # Extract the values from the cName column as a list
        cName_list = row['cName'][1:-1].split(", ")
        cName_list = [re.sub('[\[\]\']', '', item) for item in cName_list]  # Remove brackets and quotes from the strings

        # Store the values in a list
        children = cName_list

        if type == "Folk":
            paganroots = "yes"
            pagandoctrine = "doctrine = unreformed_faith_doctrine"
        else:
            paganroots = "no"


        # Check if the value in column i is 0
        if value == 0:
            family = "rf_pagan"
            doc_hostile = random.choice(['pagan_hostility_doctrine', 'abrahamic_hostility_doctrine'])
            doc_hof = random.choice(['doctrine_no_head', 'doctrine_spiritual_head'])
            doc_tolerance = "doctrine_pluralism_pluralistic"
            doc_holdings = "doctrine_theocracy_temporal"
            doc_marriage = random.choice(['doctrine_monogamy', 'doctrine_polygamy', 'doctrine_concubines'])
            doc_divorce = random.choice(
                ['doctrine_divorce_disallowed', 'doctrine_divorce_approval', 'doctrine_divorce_allowed'])
            doctrine_bastardry = random.choice(
                ['doctrine_bastardry_none', 'doctrine_bastardry_legitimization', 'doctrine_bastardry_all'])
            doctrine_homosexuality = "doctrine_homosexuality_accepted"
            doctrine_deviancy = random.choice(
                ['doctrine_deviancy_crime', 'doctrine_deviancy_shunned', 'doctrine_deviancy_accepted'])
            doctrine_adultery_men = random.choice(
                ['doctrine_adultery_men_crime', 'doctrine_adultery_men_shunned', 'doctrine_adultery_men_accepted'])
            doctrine_adultery_women = random.choice(
                ['doctrine_adultery_women_crime', 'doctrine_adultery_women_shunned', 'doctrine_adultery_women_accepted'])
            doctrine_kinslaying = random.choice(
                ['doctrine_kinslaying_any_dynasty_member_crime', 'doctrine_kinslaying_extended_family_crime',
                 'doctrine_kinslaying_shunned', 'doctrine_kinslaying_close_kin_crime', 'doctrine_kinslaying_accepted'])
            doctrine_witchcraft = random.choice(
                ['doctrine_witchcraft_crime', 'doctrine_witchcraft_shunned', 'doctrine_witchcraft_accepted'])
            doctrine_gender = random.choice(
                ['doctrine_gender_male_dominated', 'doctrine_gender_equal', 'doctrine_gender_female_dominated'])
            doctrine_consanguinity = random.choice(['doctrine_consanguinity_restricted', 'doctrine_consanguinity_cousins',
                                                    'doctrine_consanguinity_aunt_nephew_and_uncle_niece',
                                                    'doctrine_consanguinity_unrestricted'])
            doctrine_pluralism = random.choice(
                ['doctrine_pluralism_fundamentalist', 'doctrine_pluralism_righteous', 'doctrine_pluralism_pluralistic'])
            doctrine_theocracy = random.choice(['doctrine_theocracy_lay_clergy', 'doctrine_theocracy_temporal'])
            doctrine_head_of_faith = random.choice(
                ['doctrine_no_head', 'doctrine_spiritual_head', 'doctrine_temporal_head'])
            doctrine_clerical_function = random.choice(
                ['doctrine_clerical_function_taxation', 'doctrine_clerical_function_alms_and_pacification',
                 'doctrine_clerical_function_recruitment'])
            doctrine_clerical_gender = random.choice(
                ['doctrine_clerical_gender_male_only', 'doctrine_clerical_gender_female_only',
                 'doctrine_clerical_gender_either'])
            doctrine_clerical_marriage = random.choice(
                ['doctrine_clerical_marriage_allowed', 'doctrine_clerical_marriage_disallowed'])
            doctrine_clerical_succession = random.choice(
                ['doctrine_clerical_succession_temporal_appointment', 'doctrine_clerical_succession_spiritual_appointment',
                 'doctrine_clerical_succession_temporal_fixed_appointment',
                 'doctrine_clerical_succession_spiritual_fixed_appointment'])
            faithcolor = color_generator()
            tenet_options = (
            ['tenet_aniconism', 'tenet_alexandrian_catechism', 'tenet_armed_pilgrimages', 'tenet_carnal_exaltation',
             'tenet_communal_identity', 'tenet_communion', 'tenet_consolamentum', 'tenet_divine_marriage',
             'tenet_gnosticism', 'tenet_mendicant_preachers', 'tenet_monasticism', 'tenet_pacifism', 'tenet_pentarchy',
             'tenet_unrelenting_faith', 'tenet_vows_of_poverty', 'tenet_pastoral_isolation', 'tenet_adaptive',
             'tenet_esotericism', 'tenet_legalism', 'tenet_literalism', 'tenet_reincarnation',
             'tenet_religious_legal_pronouncements', 'tenet_struggle_submission', 'tenet_false_conversion_sanction',
             'tenet_tax_nonbelievers', 'tenet_asceticism', 'tenet_bhakti', 'tenet_dharmic_pacifism', 'tenet_inner_journey',
             'tenet_ritual_hospitality', 'tenet_adorcism', 'tenet_ancestor_worship', 'tenet_astrology', 'tenet_hedonistic',
             'tenet_human_sacrifice', 'tenet_mystical_birthright', 'tenet_ritual_celebrations', 'tenet_sacred_childbirth',
             'tenet_sanctity_of_nature', 'tenet_sky_burials', 'tenet_sun_worship', 'tenet_gruesome_festivals',
             'tenet_exaltation_of_pain', 'tenet_natural_primitivism', 'tenet_pursuit_of_power', 'tenet_ritual_cannibalism',
             'tenet_sacred_shadows', 'tenet_polyamory'])
            icon_options = (
            ["antler", "celtic_01", "celtic_02", "celtic_03", "celtic_04", "oak_01", "oak_02", "viking_01", "viking_02",
             "viking_03", "viking_04", "viking_05", "viking_06"])

            tenet1 = random.choice(tenet_options)
            tenet_options.remove(tenet1)
            tenet2 = random.choice(tenet_options)
            tenet_options.remove(tenet2)
            tenet3 = random.choice(tenet_options)

            f1tenet1 = random.choice(tenet_options)
            tenet_options.remove(f1tenet1)
            f1tenet2 = random.choice(tenet_options)
            tenet_options.remove(f1tenet2)
            f1tenet3 = random.choice(tenet_options)

            # processes outputs of individual faith of one family
            outputs = []
            for child in children:
                faithcolor = color_generator()
                if any(c.isalpha() for c in child):
                    child = re.sub(r'\W+', '', child).lower()  # remove non-alphanumeric characters and spaces
                    output = f"{child} = {{ "
                    outputs.append(output)

            # outputs into text each faith
            # full_text = "\n\n\t\t".join(["{}{}{}{}{}{}{}{}{}{}".format(output,"\n\t\tcolor = ",faithcolor, "\n\t\tdoctrine = ", random.choice(tenet_options), "\n\t\tdoctrine = ", random.choice(tenet_options), "\n\t\tdoctrine = ", random.choice(tenet_options),"\n\t\t}") for index, output in enumerate(outputs)])
            # outputs into text each faith
            full_text = "\n\n\t\t".join([
                # If adding more Variables below, make sure to add {}
                "{}{}{}{}{}{}{}{}{}{}{}{}".format(
                    output, "\n\t\tcolor = ",
                    "{{ {:.2f} {:.2f} {:.2f} }}".format(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
                    "\n\t\ticon = ", random.choice(icon_options),
                    "\n\t\tdoctrine = ", random.choice(tenet_options),
                    "\n\t\tdoctrine = ", random.choice(tenet_options),
                    "\n\t\tdoctrine = ", random.choice(tenet_options),
                    "\n\t\t}"

                ) for output in outputs
            ])

            # Write the name to a text file with "00_" at the start
            file_name = f"00_{mainFamName}.txt"
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "w", encoding="utf-8-sig") as file:
                file.write(f"{mainFamName}_religion = {{\n\tfamily = rf_{mainFamName}"
                           f"\n\tdoctrine = {doc_hostile}"
                           f"\n\tpagan_roots = {paganroots}\n"
                           f"\n\tdoctrine = {doctrine_head_of_faith}"
                           f"\n\tdoctrine = {doctrine_gender}"
                           f"\n\tdoctrine = {doctrine_pluralism}"
                           f"\n\tdoctrine = {doctrine_theocracy}"
                           f"\n\tdoctrine = {doc_marriage}"
                           f"\n\tdoctrine = {doc_divorce}"
                           f"\n\tdoctrine = {doctrine_bastardry}"
                           f"\n\tdoctrine = {doctrine_consanguinity}"
                           f"\n\tdoctrine = {doctrine_homosexuality}"
                           f"\n\tdoctrine = {doctrine_adultery_men}"
                           f"\n\tdoctrine = {doctrine_adultery_women}"
                           f"\n\tdoctrine = {doctrine_kinslaying}"
                           f"\n\tdoctrine = {doctrine_deviancy}"
                           f"\n\tdoctrine = {doctrine_witchcraft}"
                           f"\n\tdoctrine = {doctrine_clerical_function}"
                           f"\n\tdoctrine = {doctrine_clerical_gender}"
                           f"\n\tdoctrine = {doctrine_clerical_marriage}"
                           f"\n\tdoctrine = {doctrine_clerical_succession}\n"
                           f"\n\ttraits ="" {\n"
                           f"\t\tvirtues =""{brave just compassionate""}"
                           f"\n\t\tsins =""{\tcraven arbitrary callous""}"
                           f"\n\t""}"
                           f"\n\tcustom_faith_icons ="" {\n"
                           f"\t\tcustom_faith_1 custom_faith_2 custom_faith_3 custom_faith_4 custom_faith_5 custom_faith_6 custom_faith_7 custom_faith_8"
                           f"\n\t""}"
                           f"\n\tholy_order_names ="" {}\n"
                           f"\n\tfaiths ="" {"
                           f"\n\t\t{mainFamName} ="" {\n"
                           f"\n\t\tcolor = {faithcolor}\n"
                           f"\n\t\ticon = {random.choice(icon_options)}\n"
                           f"\n\t\tdoctrine = {tenet1}\n"
                           f"\n\t\tdoctrine = {tenet2}\n"
                           f"\n\t\tdoctrine = {tenet3}\n"
                           f"\t\t{pagandoctrine}\n"
    
                           "\t\t}\n"
                           f"\n\t\t{full_text}\n"
    
                           "}\n"
    
    
    
    
    
    
    
                           f" \n}}")


#familyGen("combined_data.xlsx")

#religionChildren("combined_data.xlsx","religionChildren.xlsx")

#relGenChil("religionChildren.xlsx","religionChildren_cName.xlsx")

#religionGen("religionChildren_cName.xlsx","common/religion/religions")