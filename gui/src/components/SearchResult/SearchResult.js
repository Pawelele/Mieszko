import classes from './SearchResult.module.css';

const SearchResult = ({ searchResult, onClick }) => {

  const searchResultClickHandler = (event) => {
    onClick(searchResult);
  }

  return (
    <div className={classes.searchResult} onClick={searchResultClickHandler}>
      <div className={classes.image}>
        <img src={searchResult.images[0]} />
      </div>
      <div className={classes.content}>
        <div className={classes.left}>
          <div className={classes.region}>
            {searchResult.city}, {searchResult.district}
          </div>
          <div className={classes.title}>
            {searchResult.title}
          </div>
          <div className={classes.data}>
            <div className={classes.area}>
              {searchResult.area} m2
            </div>
            <div className={classes.rooms}>
              {searchResult.rooms} pokoje
            </div>
          </div>
        </div>
        <div className={classes.right}>
          <div className={classes.price}>
            {searchResult.price} zł
          </div>
          <div className={classes.pricePerMeter}>
            {searchResult.pricePerMeter} zł/m2
          </div>
        </div>
      </div>
    </div>
  );
};

export default SearchResult;