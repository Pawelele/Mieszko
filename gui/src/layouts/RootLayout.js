import { Outlet } from 'react-router-dom';
import classes from './RootLayout.module.css';
import MainNavigation from '../components/MainNavigation/MainNavigation';
import ColoredLine from '../components/ColoredLine/ColoredLine';
import Footer from '../components/Footer/Footer';

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
        <Footer />
      </div>
    </div>
  )
}

export default RootLayout;