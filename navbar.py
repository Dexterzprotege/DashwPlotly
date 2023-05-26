import dash_bootstrap_components as dbc
# import dash_html_components as html
from dash import html, dcc

TESLA_LOGO = "res/tesla-logo-png-2231.png"
def create_navbar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=TESLA_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                # dcc.Link(
                #     dbc.NavbarBrand("Navbar", className="ml-2"),
                #     href="/",
                # ),
                dbc.Nav(
                    [
                        dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
                        dbc.NavItem(dcc.Link("About", href="/about", className="nav-link")),
                        dbc.NavItem(dcc.Link("Contact", href="/contact", className="nav-link")),
                    ],
                    className="ml-auto",
                    navbar=True,
                ),
            ],
        ),
        color="dark",
        dark=True,
    )

    return navbar
