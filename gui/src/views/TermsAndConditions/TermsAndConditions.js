import classes from './TermsAndConditions.module.css';

const TermsAndConditions = () => {
    return (
        <div className={classes.wrapper}>
            <h1>Regulamin</h1>
            <p className={classes.paragraph}>
                Witaj na naszej stronie. Jeżeli kontynuujesz przeglądanie i korzystanie z tej strony, zgadzasz się przestrzegać i być związany następującymi warunkami korzystania, które razem z naszą polityką prywatności regulują naszą relację z Tobą w odniesieniu do tej strony.
            </p>
            <p className={classes.paragraph}>
                Termin "firma", "nas", "my" odnosi się do właściciela strony, a termin "Ty" odnosi się do użytkownika lub widza naszej strony.
            </p>
            <p className={classes.paragraph}>
                Korzystanie z tej strony podlega następującym warunkom korzystania:
            </p>
            <ul className={classes.list}>
                <li>Strona zawiera materiały, które są własnością lub licencjonowane przez nas. Te materiały obejmują, ale nie ograniczają się do, designu, układu, wyglądu i grafiki. Powielanie jest zabronione, chyba że zgodnie z notatką o prawach autorskich, która jest częścią tych warunków.</li>
                <li>Nieprawidłowe korzystanie z tej strony może skutkować roszczeniem o odszkodowanie lub być przestępstwem.</li>
                <li>Od czasu do czasu ta strona może zawierać również linki do innych stron. Te linki są dostarczane dla Twojej wygody, aby zapewnić dalsze informacje. Nie oznaczają, że popieramy te strony. Nie mamy odpowiedzialności za treść powiązanych stron.</li>
            </ul>
            <p className={classes.paragraph}>
                Twój korzystanie z tej strony i wszelkie spory wynikające z takiego korzystania z strony podlegają prawom Polski.
            </p>
        </div>
    );
}

export default TermsAndConditions;
