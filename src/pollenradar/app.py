import streamlit as st


def main() -> None:
    st.set_page_config(
        page_title="PollenRadar Analytics",
        layout="wide",
    )

    st.title("PollenRadar Analytics")
    st.write("Analyse und Visualisierung von Pollendaten.")

    dashboard, analyse, visualisierung, datenimport = st.tabs(
        [
            "Dashboard",
            "Datenanalyse",
            "Visualisierung",
            "Datenimport",
        ]
    )

    with dashboard:
        st.header("Dashboard")
        st.info("Hier wird später eine Übersicht der Pollendaten angezeigt.")

    with analyse:
        st.header("Datenanalyse")
        st.info("Hier werden später statistische Auswertungen angezeigt.")

    with visualisierung:
        st.header("Visualisierung")
        st.info("Hier werden später Diagramme und Vergleiche angezeigt.")

    with datenimport:
        st.header("Datenimport")
        st.info("Hier können später API- oder CSV-Daten geladen werden.")


if __name__ == "__main__":
    main()
