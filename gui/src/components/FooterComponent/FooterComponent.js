import classes from './FooterComponent.module.css';
import logo from '../../assets/img/logo.png';
import { NavLink } from 'react-router-dom';

const FooterComponent = () => {
  return (
    <footer className={classes.wrapper}>
      <div className={classes.logo}>
        <img src={logo} />
      </div>
      <div className={classes.content}>
        <NavLink to="/">Strona główna</NavLink>
        <NavLink to="/onas">O nas</NavLink>
        <NavLink to="/regulamin">Regulamin</NavLink>
        <NavLink to="/kontakt">Kontakt</NavLink>
      </div>
      <div className={classes.text}>
        2023 Mieszko. Wszelkie prawa zastrzezoneC.
      </div>
    </footer>
  )
}

export default FooterComponent;