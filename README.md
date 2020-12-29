# Radiation Test Results

[**www.radtestresults.com**](http://www.radtestresults.com)

Radiation testing is ludicrously expensive and difficult. I work in the aerospace industry and I wanted to help folks get over the initial struggles I had when I began. This is a little web app that might help people who are looking to get started with what is available to them if they want to design electronics for space. A lot of this data is available right now, but not in an accessible way, and it requires tons of (repeated) overhead to understand what you're looking at. It seems this was somewhat available on the NSREC website at `http://www.nsrec.com/redw/` but doesn't seem to be anymore unfortunately. Regardless, this new format is hopefully more helpful to aerospace engineers and potential new ones.

This also requires the "obligatory disclaimer": just because one person tested something once doesn't mean you should go buy 100 of those parts and put them in your design. Do your own homework, read the report, test again, or just launch in LEO.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. This assumes you have Python 3.5+ (haven't tested outside 3.5, but I assume it won't break, let me know if it does).

1. First, clone the project:

    ```
    git clone https://github.com/bradysalz/rad-test-results.git
    ```

2. Install dependencies

    ```
    apt install libsqlite3-dev
    ```

3. Setup a virtual environment

    ```
    cd rad-test-results
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the Python requirements

    ```
    pip install -r requirements.txt
    ```

5. If you wish to go through the data collection process, see below.

6. Run the web app

    ```
    python app.py
    ```

7. You should now have the website live at `locahost:6543`


## License

The web app is MIT licensed (see [LICENSE](LICENSE)).

## Citations

The data is sourced from a variety of places, but primarily the IEEE NSREC Radiation Effects Data Workshop. Primary data sources are cited in [CITATIONS.bib](CITATIONS.bib). Note those often point to many individual specific papers, which are cited on the web app on a per part basis.

## Acknowledgements

Many thanks to the following groups for this:

* [IEEE NSREC](http://www.nsrec.com/) for delibrately hosting a venue to allow open information exchange
* [David Hiemstra](https://ieeexplore.ieee.org/author/37273132000) for tirelessly putting together summarized reports
