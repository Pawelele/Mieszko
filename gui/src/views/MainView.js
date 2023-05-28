import classes from './MainView.module.css'
import logo from '../assets/img/logo.png';
import { NavLink } from 'react-router-dom';

const MainView = () => {
  return (
    <div className={classes.wrapper}>
      <div className={classes.mainContent}>
        <img src={logo} className={classes.logo} />
        <h1 className={classes.title}>Znajdź swoje nowe mieszkanie w najlepszej cenie</h1>
        <NavLink to='/mieszkania'><button className={classes.button}>Szukaj</button></NavLink>
      </div>
    </div>
  );
}

export default MainView;