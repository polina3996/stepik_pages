# stepik_pages

Project of PageObject pattern of testing.
 
The project has conftest file with fixture of opening and closing browser-window and getting inputted language of the page, that can be chosen by you, and pytest.ini file with registrated marks of tests.

There is BasePage class, that is parent to all page-classes. Contains common and technical methods(creating page-object, opening web-page, checking if element is present or not, if element diasappears after some time, etc.)

Also there are 4 classes of tested web-pages(Basket-, Product-, Login- and MainPage) with their assertion methods.

2 files with different test-cases test Main page and Product page respectively. Test cases are united in classes thematically and marked so.

There is also 1 file with all needed selectors and the way we search for it, united into cortage and unpacked later in corresponded methods.





