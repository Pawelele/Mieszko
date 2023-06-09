import classes from './AboutUs.module.css';

const AboutUs = () => {
    return (
        <div className={classes.wrapper}>
            <h1>O nas</h1>
            <p className={classes.paragraph}>
                Jesteśmy dynamicznym zespołem specjalistów z pasją do technologii i nieruchomości. Nasza firma, będąca porównywarką cen mieszkań, została stworzona, aby ułatwić Ci proces poszukiwania idealnego miejsca do życia.
            </p>
            <p className={classes.paragraph}>
                Nasza misja to dostarczanie najaktualniejszych i najbardziej wiarygodnych informacji o cenach mieszkań w całej Polsce. Dzięki współpracy z różnymi stronami internetowymi, takimi jak Ceneo, jesteśmy w stanie zapewnić Ci najszerszy wybór ofert na rynku.
            </p>
            <p className={classes.paragraph}>
                Stale inwestujemy w technologię i innowacje, aby nasza platforma była łatwa w obsłudze, szybka i bezpieczna. Naszym priorytetem jest zadowolenie użytkowników i to dla Was stale się rozwijamy.
            </p>
            <p className={classes.paragraph}>
                Zapraszamy do korzystania z naszej strony, a w razie jakichkolwiek pytań lub sugestii, skontaktuj się z nami. Cenimy Twoją opinię i jesteśmy tutaj, aby Ci pomóc.
            </p>
        </div>
    )
}

export default AboutUs;