import logo from '../../assets/img/logo.png';
import { Link, NavLink } from 'react-router-dom';
import classes from './MainNavigation.module.css';

const MainNavigation = () => {
  return (
    <header className={classes.wrapper}>
      <Link to="/"><div className={classes.logo}><img src={logo} /></div></Link>
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
            <NavLink to="/onas" activeClassName="active">
              <button className={classes.button}>O nas</button>
            </NavLink>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;