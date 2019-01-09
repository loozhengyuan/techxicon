# Techxicon

Techxicon is a tech dictionary created with emphasis on simplified definitions and contextualised examples to the public service where relevant.

It is a pilot project by Digital Capabilities Team at Civil Service College, with the aim of establishing a common 'digital' language between public officers. We envision Techxicon to be a one-stop resource where public officers can search, learn, and explore technology terms and processes.

##### Features
- 200+ technology-related terms that you can search to know more about 
- Contextualised definitions and examples related to the public service
- Community-contributed definitions/resources
- Wikipedia-style link surfing

##### Architecture
- Built on Python & Django
- Data storage on Postgres
- Full-text-search via Postgres
- Runs on Gunicorn
- Web requests handled by Caddy

## Roadmap

### Suggested Features
- Fuzzy search (For search with wrong spellings)
- Citations for each term
- Word-of-the-day
- 24hr word cloud
- Mouseover pop-up for hyperlinks (Using AJAX/JQuery?)
- Search completion 

## Acknowledgements

Many content posted here comes from a wealth of resources available on DigitalOcean's [docs](https://www.digitalocean.com/docs/) and [tutorials](https://www.digitalocean.com/community/tutorials) page. In addition, Django also provides a very very good [documentation](https://docs.djangoproject.com/en/2.0/) on the framework. 

Much of the feedback and word improvements are contributed by the search history and user feedback from Public Service officers. Thank you for helping us to improve the Techxicon!
 
## License

This project is licensed under the GNU GPLv3 License
