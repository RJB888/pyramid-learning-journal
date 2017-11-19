Create a TEST_PLAN.md file in your project root that lists out every test you intend to run and what that test is looking for.
TEST_PLAN.md should encompass not just the tests you intend to write for the create and update views, but every test you’ve written thus far. I want to see your thought process.
TEST_PLAN.md will need to be updated as you update your code next week. Keep it current!

##Unit Testing

Test list_view response - 
    This will test the list view returns what we tell it to return.

Test list_view response data type - 
    This will test what the list view returns to make sure its a dict.

Test list_view response image - 
    Test to make sure the image returned by the list view is the proper image.

Test detail_view response -
    Test that the detail view response sends the proper post title.

Test detail_view response keys- 
    Make sure the detail view response is sending the proper keys for the dict values.

Test create_view response - 
    Test that the create view sends the proper response title back.

Test creat_view can take specific id -
    Test that when give a specific id, create view functions and sends back a response.

Test update_view loads page when given an id -
    Test update view to make sure it loads properly and sends a response back.

Test update_view "placeholder" content - 
    Test the update_view to make sure it loads the placeholder content from the intended blog post.

Test detail_view raisis HTTPNotFound - 
    Test that when given a bad request, detail view raises the appropriate HTTPNotFound error.

Test update_view for HTTPNotFound -
    Test that when given a bad request, update view raises appropriate HTTPNotFound error.

## Functional Testing

Test that when the home route for 200 response - 
    Test the when the home route is hit by the app it send a 200 Ok status.

Test detail_view - 
    Test the detail view to make sure it displays the desired journal entry.

Test detail view error -
    Test that the detail view raises the appropriate error when given a bad request.

Test home route display -
    Test that the home route diplays all the journal entries properly.

Test update_view display - 
    Test the update view to see that it properly pre-populates the fields with the info to be edited.

Test update_view functionality- 
    Test that the update view updates the appropriate entry in the database when given a post req. 

Test create_view display - 
    Test that create view displays template properly.

Test create_view POST - 
    Test that create view adds new entry to database with POST call.

Test create_view redirect - 
    Test that the create view send user back to the home page after entry is added to database.

Test update_view redirect - 
    Test that the update view redirects to the proper detail page after database update.

Test login allows access to update and edit routes - 
    Test that once logged in you can make or edit an entry.

Test that you cannot make an entry or update an entry unless logged in -
    Test that update rout and edit route give 403 error if not logged in.

