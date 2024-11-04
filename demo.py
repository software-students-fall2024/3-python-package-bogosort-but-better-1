from bohancompliment import ComplimentGenerator

def main():
    cg = ComplimentGenerator()
    
    #sample name and trait
    name = "Alex"
    trait = "problem-solving skills"
    
    print("=== ComplimentGenerator Demo ===\n")
    
    #generate a random compliment
    print("1. Random Compliment:")
    try:
        compliment = cg.compliment(name)
        print(f"- {compliment}\n")
    except Exception as e:
        print(f"Error: {e}\n")
    
    #generate a personalized compliment based on a trait
    print("2. Personalized Compliment:")
    try:
        personalized = cg.personalized_compliment(name, trait)
        print(f"- {personalized}\n")
    except Exception as e:
        print(f"Error: {e}\n")
    
    #generate multiple compliments
    print("3. Multiple Compliments:")
    count = 3
    try:
        compliments = cg.multi_compliment(name, count)
        for idx, comp in enumerate(compliments, 1):
            print(f"  {idx}. {comp}")
        print()
    except Exception as e:
        print(f"Error: {e}\n")
    
    #generate a compliment in a specific language
    print("4. Compliment in Different Languages:")
    languages = ['en', 'es', 'fr', 'de', 'it', 'jp']  #including an unsupported language 'jp'
    for lang in languages:
        try:
            comp_lang = cg.compliment_in_language(name, lang)
            print(f"- [{lang}] {comp_lang}")
        except Exception as e:
            print(f"- [{lang}] Error: {e}")
    print()
    
    #add a new compliment
    print("5. Adding a New Compliment:")
    new_compliment = "{name}, your innovative ideas are game-changers!"
    try:
        cg.add_compliment(new_compliment)
        print(f"- Added new compliment: \"{new_compliment}\"\n")
    except Exception as e:
        print(f"Error: {e}\n")
    
    #verify the new compliment is added
    print("   Verifying the new compliment:")
    try:
        new_comp = cg.compliment(name)
        print(f"   - {new_comp}\n")
    except Exception as e:
        print(f"   Error: {e}\n")
    
    #add a new translation
    print("6. Adding a New Translation (Portuguese):")
    new_language = 'pt'
    new_translations = [
        "Você é incrível, {name}!",
        "{name}, você torna o mundo um lugar melhor!",
        "Seu sorriso ilumina o dia de todos, {name}!",
        "Você é um verdadeiro amigo, {name}!",
        "Sua inteligência é impressionante, {name}!",
        "Você tem uma mente brilhante, {name}!",
        "{name}, sua dedicação é inspiradora!",
        "Você é uma estrela brilhante, {name}!",
        "Sua paixão pela tecnologia é contagiante, {name}!",
        "{name}, você se destaca em cada projeto que realiza!",
    ]
    try:
        cg.add_translation(new_language, new_translations)
        print(f"- Added new language '{new_language}' with compliments.\n")
    except Exception as e:
        print(f"Error: {e}\n")
    
    #verify the new translation is added
    print("   Verifying the new translation:")
    try:
        pt_comp = cg.compliment_in_language(name, 'pt')
        print(f"   - [pt] {pt_comp}\n")
    except Exception as e:
        print(f"   Error: {e}\n")
    
    #list available languages
    print("7. Listing Available Languages:")
    try:
        languages_available = cg.list_languages()
        print(f"- Supported languages: {', '.join(languages_available)}\n")
    except Exception as e:
        print(f"Error: {e}\n")
    
    print("=== Demo Completed ===")

if __name__ == "__main__":
    main()



