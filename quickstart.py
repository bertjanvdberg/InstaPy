""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = '42eneenbeetje'
insta_password = 'Bertjan123!'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # activity
    session.follow_by_tags(['hardlopenisleuk', 'rotterdammarathon', 'ikloophard', 'duurloop'], amount=15)
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.like_by_tags(['hardlopenisleuk', 'rotterdammarathon', 'ikloophard', 'duurloop'], amount=10, interact=True)
    session.follow_commenters(['running_wout', 'gaby_runs_the_world'], amount=100, daysold=2, max_pic = 10, sleep_delay=600, interact=False)
