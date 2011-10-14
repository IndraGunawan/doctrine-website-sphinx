:author: avalanche123 <mallluhuct@gmail.com>
:date: 2010-07-22 11:57:00

==================================
MongoDB ODM: MongoDB for eCommerce
==================================


.. raw:: html

   <div style="float: left; width: 300px;">
       <div style="padding: 15px; border: 1px solid #ccc; margin: 0 15px; background: #eee; color: #888">
       <p style="margin: 0;">
   
Hi, my name is Bulat S. (my last name won't make it any easier, but
in case you were wondering it's Shakirzyanov), I joined OpenSky in
August 2009 (It's been almost a year since then, but it feels like
ages). My official title in the company is Hacker, which also says
a lot about me (that I don't like corporate titles for one).

.. raw:: html

   </p>
       <p style="margin: 10px 0 0;">
   
The last 6 weeks were truly amazing for me. Not only was I able to
learn a new technology, I also managed to contribute back to the
community. But let's go over everything step by step.

.. raw:: html

   </p>
       </div>
   </div>
   
Building an eCommerce system is not easy, and building a platform
is even harder. When it comes to data in eCommerce, there is
nothing definite, no real structure you could stick to, and no
final requirements. Something as obvious as the "item you add to
cart" could be overly complicated when it comes to data.

There is a good example of how to model the database for handling
variable product attributes;
`Magento <http://www.magentocommerce.com>`_ is one of the most
advanced open source eCommerce solutions available today. It uses
`EAV (Entity Attribute Value) <http://en.wikipedia.org/wiki/Entity-attribute-value_model>`_,
which solves the problem of variable attributes by sacrificing
database level integrity and application performance. The amount of
queries you need to perform to select one entity will grow with
every attribute data type you introduce; however, it still is a
viable solution.

A document store on the other hand lets you save two absolutely
different documents in the same collection. Because of its
schema-less structure it is also possible to add or remove a
document's properties after saving - it's a database that adapts to
your data structure on the fly.

At `OpenSky <http://www.theopenskyproject.com/>`_, we decided to
use `MongoDB <http://www.mongodb.org/>`_ for storage of products
and use relational databases for order-related data since
`MongoDB <http://www.mongodb.org/>`_ doesn't support transactions.

So what is the benefit of using
`MongoDB <http://www.mongodb.org/>`_ over MySQL, or any other
RDBMS, for storing variable attribute data. Performance. This is
the pseudo-query we would have to write to select one product, with
id 1, and all of its attributes in a typical
`EAV model <http://en.wikipedia.org/wiki/Entity-attribute-value_model>`_:


.. raw:: html

   <div class="right">
       
   

.. raw:: html

   </div>
   
::

    [txt]
    SELECT * FROM `product` WHERE id = 1;
    SELECT * FROM `product_attributes` = WHERE product_id = 1;
    SELECT * FROM `product_values_int` WHERE product_id = 1;
    SELECT * FROM `product_values_varchar` WHERE product_id = 1;
    SELECT * FROM `product_values_datetime` WHERE product_id = 1;
    SELECT * FROM `product_values_text` WHERE product_id = 1;
    SELECT * FROM `product_values_float` WHERE product_id = 1;

After the above queries are run, there would be a huge step of data
hydration into the product object, which
`Magento <http://www.magentocommerce.com>`_ handles quite well,
albeit slowly. Contrast this with what we would do in
`MongoDB <http://www.mongodb.org/>`_:

::

    [javascript]
    db.products.find({'_id': '1'});

Not only is the selection simpler, but it also returns a JSON
object, which can easily be hydrated into a native PHP object. And
here is how a configurable product could be represented in
`MongoDB <http://www.mongodb.org/>`_:

::

    [javascript]
    {
        "_id": ObjectId("4bffd798fdc2120019040000")
        "name": "Configurable T-Shirt"
        "options": [
            {
                "name": "small",
                "price": 12.99
            },
            {
                "name": "medium",
                "price": 15.99
            },
            {
                "name": "large",
                "price": 17.99
            }
        ]
    }

    **NOTE** There is no need for joins, as product options are a
    collection of embedded objects. Object references (akin foreign key
    relationships in RDBMSs) are also possible, but they are generally
    only necessary if you need to access the object independently. For
    instance, if I needed a page to list all product options across all
    products, I would probably put options into their own collection
    and reference them from the product document.


Of course, there are
`plenty of ORM libraries <http://www.mongodb.org/display/DOCS/PHP+Language+Center#PHPLanguageCenter-LibraryandFrameworkTools>`_
for `MongoDB <http://www.mongodb.org/>`_, which were either
hard-to-extract parts of frameworks, not quite ORMs or used the
`ActiveRecord pattern <http://martinfowler.com/eaaCatalog/activeRecord.html>`_
(which after using
`DataMapper <http://martinfowler.com/eaaCatalog/dataMapper.html>`_
for quite some time, I wouldn't want to go back to). The very same
day I started writing an object document mapper (ODM) to use at
`OpenSky <http://www.theopenskyproject.com/>`_,
`Jon Wage <http://www.twitter.com/jwage>`_ (developer for the
Doctrine project) released a proof-of-concept
`MongoDB ODM <http://www.doctrine-project.org/projects/mongodb_odm>`_,
which you can
`find on github <http://github.com/doctrine/mongodb-odm>`_. After
contacting Jon and giving his library a couple of tries and
`tests <http://www.phpunit.de/>`_, I decided to use it for
`OpenSky <http://www.theopenskyproject.com/>`_'s products domain
layer.

I started to submit patches and
`unit tests <http://www.phpunit.de/>`_ to the project and soon
joined the core team for
`MongoDB ODM <http://www.doctrine-project.org/projects/mongodb_odm>`_.
Today, we are past first alpha release of the project, and this is
my first post on the Doctrine blog (yay!).

Getting back to our example, this is how the product and embedded
option classes for the aforementioned data structure could look:

::

    [php]
    // Product.php
    /**
     * @Document(collection="products")
     */
    class Product
    {
    
        /**
         * @Id
         */
        private $id;
    
        /**
         * @String
         */
        private $name;
    
        /**
         * @EmbedMany(targetDocument="Product\Option")
         */
        private $options = array();
    
        public function getId()
        {
            return $this->id;
        }
    
        public function setName($name)
        {
            $this->name = $name;
        }
    
        public function getName()
        {
            return $this->name;
        }
    
        public function addOption(Product\Option $option)
        {
            $this->options[] = $option
        }
    
        //...
    }

And the Product class:

::

    [php]
    // Product/Option.php
    namespace Product;
    /**
     * @EmbeddedDocument
     */
    class Option
    {
    
        /**
         * @String
         */
        private $name;
    
        /**
         * @Float
         */
        private $price;
    
        public function setName($name)
        {
            $this->name = $name;
        }
    
        public function getName()
        {
            return $this->name;
        }
    
        public function setPrice($price)
        {
            $this->price = $price;
        }
    
        public function getPrice()
        {
            return $this->price;
        }
    
        //...
    }

Using the DocumentManager instance, we could easily persist the
product with:

::

    [php]
    $product = new Product();
    $product->setName('Configurable T-Shirt');
    
    $small = new Product\Option();
    $small->setName('small');
    $small->setPrice(12.99);
    $product->addOption($small);
    
    $medium = new Product\Option();
    $medium->setName('medium');
    $medium->setPrice(15.99);
    $product->addOption($medium);
    
    $large = new Product\Option();
    $large->setName('large');
    $large->setPrice(15.99);
    $product->addOption($large);
    
    $documentManager->persist($product);
    $documentManager->flush();

    **NOTE** MongoDB ODM intelligently uses
    `atomic operators <http://www.mongodb.org/display/DOCS/Atomic+Operations>`_
    to update data, which makes it really fast. It also supports
    inheritance (collection-per-class and single-collection
    inheritances), which is similar to table inheritance design
    patterns for ORMs. Check out the official Mongo ODM
    `project documentation <http://www.doctrine-project.org/projects/mongodb_odm/1.0/docs/en>`_
    for more information and examples. Complete instructions on how to
    setup your DocumentManager instance
    `can be found here <http://www.doctrine-project.org/projects/mongodb_odm/1.0/docs/reference/introduction/en>`_.


The above code would store the product object as a document in
`MongoDB <http://www.mongodb.org/>`_.

There is much more to talk about in terms or technologies,
techniques and practices we adopt and use at
`OpenSky <http://www.theopenskyproject.com/>`_, so this post is
definitely not the last one.


