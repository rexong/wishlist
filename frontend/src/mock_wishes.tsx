const wishes = [
  {
    title: "Customized jewelry",
    description: "Personalized pieces, like engraved necklaces or birthstone rings.",
    link: "https://www.etsy.com/market/custom_jewelry",
    is_hidden: false
  },
  {
    title: "Wireless earbuds",
    description: "Cord-free audio convenience for on-the-go music and calls.",
    link: "https://www.amazon.com/s?k=wireless+earbuds",
    is_hidden: false
  },
  {
    title: "Personalized photo album",
    description: "Cherished memories in a customized and beautifully crafted album.",
    link: "https://www.shutterfly.com/photo-books",
    is_hidden: false
  },
  {
    title: "Spa gift basket",
    description: "Relaxation essentials, such as bath salts, candles, and lotions.",
    link: "https://www.amazon.com/s?k=spa+gift+basket",
    is_hidden: false
  },
  {
    title: "Cooking class or workshop",
    description: undefined,
    link: "https://www.airbnb.com/s/experiences/cooking",
    is_hidden: false
  },
  {
    title: "High-quality coffee or tea set",
    description: "Gourmet beverages with stylish accessories.",
    link: undefined,
    is_hidden: true
  },
  {
    title: "Fitness tracker",
    description: "Monitor and improve health with a wearable fitness device.",
    link: "https://www.bestbuy.com/site/wearable-technology/fitness-trackers/pcmcat332800050000.c?id=pcmcat332800050000",
    is_hidden: false
  },
  {
    title: "A good book by their favorite author",
    description: undefined,
    link: undefined,
    is_hidden: false
  },
  {
    title: "Smart home devices",
    description: "Automation and control for a connected living space.",
    link: "https://www.amazon.com/s?k=smart+home+devices",
    is_hidden: false
  },
  {
    title: "Gourmet chocolate assortment",
    description: undefined,
    link: "https://www.godiva.com/chocolate-boxes",
    is_hidden: false
  },
  {
    title: "Outdoor adventure gear",
    description: "Durable equipment for hiking, camping, or exploring.",
    link: undefined,
    is_hidden: false
  },
  {
    title: "Subscription to a streaming service",
    description: "Access to a wide range of movies and shows.",
    link: "https://www.netflix.com/",
    is_hidden: false
  },
  {
    title: "Board games or puzzles",
    description: undefined,
    link: "https://www.target.com/c/board-games-puzzles-toys/-/N-5xt9v",
    is_hidden: false
  },
  {
    title: "Customized artwork or prints",
    description: "Unique and personal pieces to decorate their space.",
    link: undefined,
    is_hidden: false
  },
  {
    title: "Cooking appliances",
    description: "Convenient kitchen tools for efficient meal preparation.",
    link: "https://www.amazon.com/s?k=kitchen+appliances",
    is_hidden: false
  },
  {
    title: "Weekend getaway or vacation package",
    description: undefined,
    link: "https://www.expedia.com/",
    is_hidden: false
  },
  {
    title: "Concert or event tickets",
    description: "Tickets to see their favorite artist or show live.",
    link: "https://www.stubhub.com/",
    is_hidden: false
  },
  {
    title: "Portable phone charger",
    description: "On-the-go power for smartphones and devices.",
    link: undefined,
    is_hidden: false
  },
  {
    title: "Personalized stationery",
    description: "Customized notepads, pens, and other writing tools.",
    link: undefined,
    is_hidden: false
  },
  {
    title: "Indoor plants or succulents",
    description: "Greenery to add life and freshness to any space.",
    link: "https://www.thesill.com/",
    is_hidden: false
  },
  {
    title: "Fitness equipment",
    description: undefined,
    link: "https://www.dickssportinggoods.com/c/fitness-equipment",
    is_hidden: false
  },
  {
    title: "Cooking or mixology classes",
    description: "Hands-on lessons to enhance culinary skills.",
    link: undefined,
    is_hidden: false
  },
  {
    title: "High-quality leather wallet or purse",
    description: "Stylish and durable accessories for daily use.",
    link: "https://www.coach.com/",
    is_hidden: false
  },
  {
    title: "Noise-canceling headphones",
    description: undefined,
    link: "https://www.bose.com/",
    is_hidden: false
  },
  {
    title: "Fashionable accessories",
    description: "Trendy additions like scarves, sunglasses, or hats.",
    link: "https://www.zara.com/",
    is_hidden: false
  },
  {
    title: "DIY craft kits",
    description: undefined,
    link: "https://www.etsy.com/",
    is_hidden: false
  },
  {
    title: "Wine or whiskey tasting experience",
    description: "Guided tastings for a refined palate.",
    link: undefined,
    is_hidden: true
  },
  {
    title: "Subscription to a magazine or book club",
    description: "Regular delivery of reading material.",
    link: "https://www.magazines.com/",
    is_hidden: false
  },
  {
    title: "Personalized cutting board or kitchen utensils",
    description: "Unique kitchen tools with a personal touch.",
    link: undefined,
    is_hidden: false
  },
  {
    title: "Art supplies",
    description: "Quality materials for painting, drawing, or other artistic pursuits.",
    link: "https://www.michaels.com/",
    is_hidden: false
  },
  {
    title: "Online courses or workshops",
    description: undefined,
    link: "https://www.udemy.com/",
    is_hidden: false
  },
  {
    title: "Smartwatch",
    description: "A versatile device for notifications, fitness tracking, and more.",
    link: "https://www.apple.com/watch/",
    is_hidden: false
  },
  {
    title: "Personalized pet accessories",
    description: "Custom items for their furry friends, like pet tags or beds.",
    link: "https://www.chewy.com/",
    is_hidden: false
  },
  {
    title: "Streaming device",
    description: undefined,
    link: "https://www.bestbuy.com/site/tv-home-theater/streaming-media-devices/pcmcat161100050040.c?id=pcmcat161100050040",
    is_hidden: false
  },
  {
    title: "Scented candles",
    description: "Delightful aromas to create a cozy atmosphere.",
    link: "https://www.bathandbodyworks.com/c/home-fragrance/all-candles",
    is_hidden: false
  },
  {
    title: "Language learning app subscription",
    description: "A gift to help them learn a new language.",
    link: "https://www.rosettastone.com/",
    is_hidden: false
  },
  {
    title: "Graphic novels or comic books",
    description: undefined,
    link: "https://www.comixology.com/",
    is_hidden: false
  },
  {
    title: "Cookbook from a favorite chef",
    description: "Inspiring recipes from a renowned culinary expert.",
    link: "https://www.amazon.com/s?k=cookbooks",
    is_hidden: false
  },
  {
    title: "Personalized tech accessories",
    description: "Customized phone cases, laptop sleeves, or mouse pads.",
    link: undefined,
    is_hidden: false
  },
  {
    title: "Yoga or fitness mat",
    description: "High-quality mats for home workouts or yoga practice.",
    link: "https://www.amazon.com/s?k=yoga+mat",
    is_hidden: false
  },
  {
    title: "Desktop indoor garden",
    description: undefined,
    link: "https://www.amazon.com/s?k=desktop+indoor+garden",
    is_hidden: false
  },
  {
    title: "Gaming accessories",
    description: "Upgrade their gaming setup with accessories like controllers, headsets, or mouse pads.",
    link: undefined,
    is_hidden: false
  },
  {
    title: "Personalized name necklace",
    description: "A stylish accessory with their name or initials.",
    link: "https://www.etsy.com/market/name_necklace",
    is_hidden: false
  }
];

export default function getWishes() {
    return wishes
}