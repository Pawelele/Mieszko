import classes from './Contact.module.css';

const Contact = () => {
  return (
    <div className={classes.wrapper}>
      <h1>Kontakt</h1>
      <p className={classes.paragraph}>
        Jesteśmy tu, aby pomóc! Skontaktuj się z nami, jeśli masz jakiekolwiek pytania.
      </p><br/>
      <div className={classes.contactInfo}>
        <h2>Informacje kontaktowe</h2>
        <p>Adres: ul. Przykładowa 15, 00-000 Warszawa, Polska</p>
        <p>Telefon: +48 123 456 789</p>
        <p>Email: info@nasza-strona.pl</p>
      </div>
      <div className={classes.contactForm}>
        <h2>Formularz kontaktowy</h2>
        <form>
          <label for="name">Imię i nazwisko:</label><br/>
          <input type="text" id="name" name="name"/><br/>
          <label for="email">Adres email:</label><br/>
          <input type="email" id="email" name="email"/><br/>
          <label for="message">Wiadomość:</label><br/>
          <textarea id="message" name="message"></textarea><br/>
          <input type="submit" value="Wyślij"/>
        </form>
      </div>
    </div>
  );
}

export default Contact;
