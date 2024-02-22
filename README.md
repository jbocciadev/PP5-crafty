# [Crafty](https://pp5-crafty-015973d8fb4f.herokuapp.com/)
##### by Juan A. Boccia
Elevate Playtime with Crafty: High-Quality Custom Toys for Children

![Crafty responsive design screenshot](readme-files/crafty-responsive-snip.PNG)

> Crafty is an e-commerce site that offers high-quality custom toys for children, designed to raise playtime to new levels. These toys are individually handcrafted with precision and care to ensure they meet the highest standards of quality. Explore Crafty's collection to enhance your child's play experience with premium personalized toys.

### [Live site](https://pp5-crafty-015973d8fb4f.herokuapp.com/) | [Repository](https://github.com/jbocciadev/PP5-crafty)

## UX and Design

Given the target audience and materials used in crafting the products, a decision was made that Crafty needed a clean, uncluttered appearence, with a soft palette of colours and a friendly, relaxed tone.

### Wireframes 
   Click [here](/readme-files/Crafty-wireframes.pdf) to view the Wireframes design for the site.

  ---

### [Colour Palette](/readme-files/crafty-palette.PNG)
  ![palette](/readme-files/crafty-palette.PNG)

  ---
### [Background imagery](/media/crafty_background.jpg)
  ![Background imagery](/media/crafty_background.jpg)

  The background image was developed using [Leonardo.ai](https://leonardo.ai/). The prompt generation tool was very helpful in narrowing down the final prompt to be used.

  ---

### Inspiration

Needless to say that this project draws heavily on the Boutique Ado walkthrough projectfrom Code Institute. Further sources for inspiration are:
  - [Etsy](https://www.etsy.com/)
  - [Smyths toys](https://www.smythstoys.com/)
  - [Odin Parker](https://odinparker.com/collections/felt-toys)
  - [Pinterest](https://www.pinterest.com/rockys2mom/childrens-felt-toys/)


## Business Model

### Overview

Crafty is a B2C e-commerce platform that provides its customers high-quality goods. The products can be grouped in 3 general categories: Toys, activity packs and party bag fillers.

Born from lengthy conversations among a group of parents concerned about their childrens' development and with an aptitude for arts and crafts, Crafty caters for children between 0 and 10 years of age. For the smaller ones, it presents a series of sensory-focused toys, where the aim is to help promote a healthy development of their minds and senses. For toddlers, it boasts a wider variety of items including puzzles and handcraft activities aimed at helping them practise and learn about the world around them in a fun, friendly way. Finally, it proposes screen-free alternatives for the older group. All products can be made-to-order and customised to suit requirements of the customers.

---
### Target Audience

The niche group Crafty aims at is comprised mostly of invested parents of young children, who take an active role in their development and are looking for alternatives to over-stimulating products, usually characterised by being composed of hard plastic, bright colours, flashing lights and loud sounds.

---
### Site aspirations

Crafty aims at presenting an easy to navigate platform, where products are clearly laid out and are easy to browse. The checkout process is swift and easy. It also allows customers to have a profile they can use to manage their relationship with the company. Customers can also contribute with reviews of the products they have purchased in the past and they can keep informed of news and developments by means of a Newsletter.

---
### Marketing

Crafty comes as a natural next-step to the development of an already established activity that has grown by word of mouth due to the creative nature and high quality of the products sold.

As is natural of other business, Crafty aims to grow, but at a sustainable rate. The fact that the products are handmade makes it unviable to maintain an agressive marketing campaign, as the company could potentially fail to meet demand and this would negatively impact the customer experience. The company already boasts a healthy customer base and is continuing to grow.

Online presence is a front that Crafty are eager to explore. Initially, this would continue to be done via word of mouth among friends and family, progressing to a wider audience. Instructional videos and reviews are in the plans as well as collaborations with schools and in specialized trade fairs.

  ### [Facebook business page](https://www.facebook.com/profile.php?id=61556590172134)
  ![facebook page](/readme-files/crafty-fb-snip.PNG)
      
  A Facebook page was created with the aim to promote the main Crafty website. Here, the main background of the site is used for the background banner, and as a profile image, a picture taken at one of our family kitchen/workshops.


## SEO

From early in the planning stage of the project, research was done on SEO-specific areas. It was immediately evident that neither demand nor competition were elevated, but this did not present an issue.
### Keywords
  See below for keyword research activity notes:

  ![notes](/readme-files/SEO-research.PNG)

---
### Links
  As a way to provide additional valuable resources to visitors and also raise chances of higher SEO ranking, links to sites by reputable and authoritative entities are provided:

  ![links](/readme-files/external-links.PNG)

---

### Sitemap and Robots

  A sitemap.xml file was created and stored in the root directory of the site for search engines to be able to find more effectively.
  Additionally, a robots.txt file was created and placed in the same location so as to enable search engines to crawl and index the site. The accounts, bag and admin apps were explicitly mentioned as they are of no value to such portals.

---

## Development

### Version control

- The chosen IDE for the development of the application was [VS Code](https://code.visualstudio.com/). Occasionally, [Gitpod](https://gitpod.io/) was used where issues were found and remote assistance was required, as well as system limitations.

- [GitHub](https://github.com) is the platform where the repository for Crafty is hosted: [Jbocciadev Crafty](https://github.com/jbocciadev/PP5-crafty).

Throughout development, the below commands were utilised to capture and store changes:
```
git add .
git commit -m "Message in quotation marks."
git push
```
additionally
```
git pull
git stash
git commit --amend
```
---

## Agile Development

From the very begining, Agile development practices were adopted so as to maintain focus and keep track of the various requirements to be delivered.

As an agile development technique, __Github Projects__ was used, taking special focus on the Kanban project board view
  > You can access the project [here](https://github.com/users/jbocciadev/projects/8).

With the "Everything is an issue" approach, Epics and User Stories were raised as project issues. These were organised in Milestones that loosely aligned with the Epics, but also included other crucial points in the development roadmap.

Issues were classified following the MOSCOW model. The labels thus assigned were continually revisited and reassessed, and a small number of them needed to be placed in the backlog and left to be implemented in a future opportunity.

### Milestones:

1. Generic issues view

![](/readme-files/Project-kb-1.PNG)

2. Basic site setup

![](/readme-files/Project-kb-2.PNG)

3. Products app

![](/readme-files/Project-kb-3.PNG)

4. Bag app

![](/readme-files/Project-kb-4.PNG)

5. Checkout and Stripe integration

![](/readme-files/Project-kb-5.PNG)

6. User Profile

![](/readme-files/Project-kb-6.PNG)

7. Advanced Products

![](/readme-files/Project-kb-7.PNG)

8. Products Reviews

![](/readme-files/Project-kb-8.PNG)

9. Contact app

![](/readme-files/Project-kb-9.PNG)

10. SEO and Legal

![](/readme-files/Project-kb-10.PNG)

---

## Under the Proverbial Hood

  ### Models
  ![Crafty ERD](/readme-files/crafty-erd.png)


  #### User
  Standard Django user model

  #### User Profile
  With a 1-1 relationship withthe User model, this model stores complementary contact details for the user.

  #### Category, Age group and Topic
  These single-field models are designed to add flexibility for site management.

  #### Product
  A major model, this stores all relevant information about the different products. There are many-to-one relationships established with the Category, Age group and Topic models.

  #### Order
  Another major model, this contains all the relevant details for the successful completion of the purchase. Maintains many-to-one relationships with the User model and one-to-many with Order line item model.

  #### Review
  This 100% custom model allows for users to submit reviews and rating of products they have purchased. Many-to-one relationships with the User and Product models.

  #### Order Line Item
  This model is crucial to maintain an ordered, itemized connection between the Product model (many OLIs can have the same product) and the Order table (one Order can contain many OLIs).

  #### Contact
  Another 100% custom model, this stores all the details for customer's queries submitted via the website. There is a many-to-one relationship with the User model.

  #### Subscriber
  A third 100% custom model, this keeps track of subscribers to the Mailbos. There are no relationships established as users and non-users can subscribe.


<!--  -->


### Reference:

Extending user model:
https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy

Django models FK on_delete:
https://sentry.io/answers/django-on-delete/

User authentication:
https://docs.djangoproject.com/en/4.2/topics/auth/default/ Login required mixin

Django Forms
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

Querying with list of values:
https://stackoverflow.com/questions/9304908/how-can-i-filter-a-django-query-with-a-list-of-values

Form querysets:
https://docs.djangoproject.com/en/4.2/ref/models/querysets/ (see Q https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.Q and select_related)

Prepopulating forms with current values:
https://studygyaan.com/django/how-to-give-initial-value-to-model-forms?utm_content=cmp-true

Getting context data:
https://docs.djangoproject.com/en/4.2/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_data

Form to update team member assignment, based on assigned team:
https://stackoverflow.com/questions/1697702/how-to-pass-initial-parameter-to-djangos-modelform-instance


Querying:
 - Field lookups: https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
 - One-to-one relationships: https://docs.djangoproject.com/en/4.2/topics/db/examples/one_to_one/

Landing page image generated using Leonardo AI:
https://leonardo.ai/

Meme generator:
https://imgflip.com/

Bootstrap icons with Django:
https://pypi.org/project/django-bootstrap-icons/

Form to update team member assignment, based on assigned team // https://stackoverflow.com/questions/1697702/how-to-pass-initial-parameter-to-djangos-modelform-instance

Database ERD:
https://dbdiagram.io/d



===


Credits:

https://ardalis.com/working-effectively-github-issues/  Epics, issues, etc

https://www.birme.net/  Images optimization for web

Leonardo.ai  AI Image generation

https://stackoverflow.com/questions/54454051/dynamic-query-django-build and https://forum.djangoproject.com/t/fielderror-related-field-got-invalid-lookup-iexact/16119/2 for building dynamic queries based on multiple criteria

# https://earthly.dev/blog/customize-django-admin-site/ 
# https://docs.djangoproject.com/en/dev/ref/models/fields/#uuidfield

# https://www.termsfeed.com/privacy-policy-generator/

# https://www.semrush.com/goodcontent/ai-text-generator/
# https://favicon.io/favicon-generator/

# https://www.smythstoys.com/

# https://stackoverflow.com/questions/35796195/how-to-redirect-to-previous-page-in-django-after-post-request

# https://www.geeksforgeeks.org/overriding-the-save-method-django-models/
# https://stackoverflow.com/questions/60481894/overwrite-django-model-init-method

# # https://stackoverflow.com/questions/29492894/how-to-remove-key-from-request-querydict-in-django

# https://stackoverflow.com/questions/74116689/how-to-count-reviews-for-a-product-in-django


# https://stackoverflow.com/questions/53801805/can-we-use-modelform-to-update-an-existing-instance-of-a-model

# https://stackoverflow.com/questions/15635790/how-to-count-the-number-of-rows-in-a-database-table-in-django#:~:text=You%20can%20either%20use%20Python's,the%20provided%20count()%20method.&text=You%20should%20also%20go%20through%20the%20QuerySet%20API%20Documentation%20for%20more%20information.


===
