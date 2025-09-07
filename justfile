default:
	cat justfile
	
install:
	pip install -e ./streamlit-i18n
	pip install -e ./streamlit-i18n-cli

# Generate dataclasses for demo project
generate:
	streamlit-i18n generate -i lib/i18n/locales/en.yml -o i18n/dataclasses_.py --rename menu=PAGES

scaffold:
	streamlit-i18n scaffold --into demo
	
# Run the Streamlit app
run-demo:
	cd demo && streamlit run Home.py
