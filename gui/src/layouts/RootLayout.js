import { Outlet } from 'react-router-dom';
import classes from './RootLayout.module.css';
import MainNavigation from '../components/MainNavigation/MainNavigation';
import ColoredLine from '../components/ColoredLine/ColoredLine';
import FooterComponent from '../components/FooterComponent/FooterComponent';

const RootLayout = () => {
  return (
    <div className={classes.wrapper}>
      <ColoredLine />
      <div className={classes.nav}>
        <MainNavigation />
      </div>
      <div className={classes.content}>
        <Outlet />
      </div>
      <div className={classes.footer}>
        <FooterComponent />
      </div>
    </div>
  )
}

export default RootLayout;