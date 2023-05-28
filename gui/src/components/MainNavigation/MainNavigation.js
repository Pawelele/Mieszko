import logo from '../../assets/img/logo.png';
import { NavLink } from 'react-router-dom';
import classes from './MainNavigation.module.css';

const MainNavigation = () => {
  return (
    <header className={classes.wrapper}>
      <div className={classes.logo}><img src={logo} /></div>
      <nav className={classes.mainNav}>
        <ul>
          <li>
            <NavLink to="/" activeClassName="active">
              <button className={classes.button}>Strona Główna</button>
            </NavLink>
          </li>
          <li>
            <NavLink to="/mieszkania" activeClassName="active">
              <button className={classes.button}>Mieszkania</button>
            </NavLink>
          </li>
          <li>
            <NavLink to="/ulubione" activeClassName="active">
              <button className={classes.button}>Ulubione</button>
            </NavLink>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;