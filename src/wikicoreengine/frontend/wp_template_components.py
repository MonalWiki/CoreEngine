"""
describes all components (nav-bar, footer,  etc) that form the pieces of a webpage on the wiki 
"""



import logging
import os
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

import ofjustpy as oj
import ofjustpy_react as ojr
from py_tailwind_utils import fw, fc, fz, gray, pd, y, ji, jc, text, mr, sb, ppos, bottom, container, H, screen, W, full




    

# def page_builder(page_key, title, builder_pagebody):

#     def view_function(request):
#         session_manager = oj.get_session_manager(request.session_id)
#         stubStore = session_manager.stubStore
#         with oj.sessionctx(session_manager):
#             with session_manager.uictx("tlctx") as tlctx:
#                 _ictx = tlctx
#                 render_nav_bar(session_manager)
#                 builder_pagebody(session_manager)
#                 render_footer(session_manager)
#                 oj.Container_("tlc", cgens= [tlctx.topper.panel, _ictx.body.panel, tlctx.footer.panel], pcp=[H/screen])
#                 wp_ = oj.WebPage_(page_key, cgens = [_ictx.tlc], title=title)

#         item_nav  = oj.PC.StackH(childs = [oj.PC.Span( text="Item views", twsty_tags=[fw.bold]),
#                                                   oj.AC.A(key="show", href="#", text="modify"),
#                                                   oj.AC.A(key="history", href="#", text="history"),
#                                                   oj.AC.A(key="Download", href="#", text="download"),
#                                                   oj.AC.A(key="delete", href="#", text="delete"),
#                                                   oj.AC.A(key="subitems", href="#", text="subitems"),
#                                                   oj.AC.A(key="discussion", href="#", text="discussion"),
#                                                   oj.AC.A(key="rename", href="#", text="rename"),
#                                                   oj.AC.A(key="highlight", href="#", text="highlight"),
#                                                   oj.AC.A(key="meta", href="#", text="Meta"),
#                                                   oj.AC.A(key="sitemap", href="#", text="Site Map"),
#                                                   oj.AC.A(key="similar", href="#", text="Similar")
#                                            ]
#                                  )        
        
#         navpanel = oj.Halign(oj.PC.StackV(childs = [top_level_nav, page_trail, item_nav]),
#                                "end")
        

#         childs = [
#             oj.AC.A(key="HomeAnchor", twsty_tags=[fc/gray/9, fz.xl, fw.extrabold],
#                   href="#", text="PutWikiTitleHere"),

#              navpanel
#         ]
#         abox = oj.PC.StackH(childs = childs, twsty_tags=[pd/y/4,  ji.center, jc.between])
#         return oj.PC.Nav(childs=[abox])

        
def render_nav_bar():
    top_level_nav = oj.PD.StackH(childs = [oj.PD.Span(key="navigation", text="Navigation", pcp=[fw.bold]), 
                                           oj.PD.A(key="history", href="#", text="History"),
                                           oj.PD.A(key="index", href="#", text="Index"),
                                           oj.PD.A(key="tags", href="#", text="Tags"),
                                           oj.PD.A(key="user", href="#", text="User"),
                                           ]
                                 )
    
    page_trail  = oj.PD.StackH(key="pagetrail",
                                      childs = [
                                          oj.PD.Span(key="title", text="Page Trail", pcp =[fw.bold])
                                      ]
                                )

    item_nav  = oj.PD.StackH("itemviews",
                              childs = [
                                  oj.PD.Span(key="itemview", text="Item views", pcp=[fw.bold]),
                                  oj.PD.Span(key="show", href="#", text="modify"),
                                  oj.PD.A(key="history", href="#", text="history"),
                                  oj.PD.A(key="Download", href="#", text="download"),
                                  oj.PD.A(key="delete", href="#", text="delete"),
                                  oj.PD.A(key="subitems", href="#", text="subitems"),
                                  oj.PD.A(key="discussion", href="#", text="discussion"),
                                  oj.PD.A(key="rename", href="#", text="rename"),
                                  oj.PD.A(key="highlight", href="#", text="highlight"),
                                  oj.PD.A(key="meta", href="#", text="Meta"),
                                  oj.PD.A(key="sitemap", href="#", text="Site Map"),
                                  oj.PD.A(key="similar", href="#", text="Similar")
                              ]
                             )

    navpanel = oj.Halign(oj.PD.StackV(key="navpanel",
                                      childs = [top_level_nav, page_trail, item_nav]),
                               "end"
                         )

    cgens = [
            oj.PD.A(key="HomeAnchor", twsty_tags=[fc/gray/9, fz.xl, fw.extrabold],
                  href="#", text="PutWikiTitleHere"),

             navpanel
        ]
    
    abox = oj.PD.StackH(key="abox", cgens = cgens,
                        twsty_tags=[pd/y/4,  ji.center, jc.between])
    
    return oj.PD.Nav(key="panel", childs=[abox])


def render_footer():
    with oj.uictx("footer") as footerbodyCtx:
        aboutcontent = oj.PC.Prose(text= "MyWiki Powered by MonalWiki Engine",
                            twsty_tags=[fz.sm, text/gray/600, pd/y/2])

        about_section = oj.PC.Subsection("About", aboutcontent)

        linkouthref = oj.PC.StackG( num_cols=3, childs = [
            oj.AC.A(key="pypower", text="Python Power", href="#"), 
            oj.AC.A(key="Licensed", text="GPL Licensed", href="#"),
            oj.AC.A(key="Monallabs", text="Developed by MonalLabs ", href="#")
        ])
        
        linkout_section = oj.PC.Subsection("", linkouthref, twsty_tags=[W/full])
        
        footer = oj.PC.Footer(childs=[oj.PC.Hr( twsty_tags=[mr/sb/4]),
                                      oj.PC.StackH(
                                               childs= [about_section, linkout_section],
                                        twsty_tags=[W/full]
                                        )
                                      
                                      ],
                              twsty_tags=[W/full]
                   )
        
        # place it at the bottom
        panel = oj.PC.StackH( childs = [footer],
                   twsty_tags=[ppos.absolute, bottom/0, W/full]
                   )

        return panel


def page_builder(page_key, title, builder_pagebody, **kwargs):
    with oj.uictx("tlctx"):
        nav_panel = render_nav_bar()
        body_panel = builder_pagebody()
        footer = render_footer()
        tlc = oj.PC.Container(childs = [nav_panel,
                                  body_panel,
                                  footer
                                  ],
                        twsty_tags =[H/screen]
                        )

        wp_template = oj.Mutable.WebPage(key=page_key,
                             childs = [tlc
                                       ],
                             title=title
                  )
        return wp_template





