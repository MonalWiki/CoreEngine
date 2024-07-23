# this needs to be imported first; else there ends up
# two copies of ofjustpy and breaks the session manager
from .wp_template_components import page_builder, render_nav_bar, render_footer



import ofjustpy as oj
import ofjustpy_react as ojr
from . import actions
from addict import Dict
from ..constant_keys import CURRENT
from ..constant_keys import ITEMTYPE_NONEXISTENT, ITEMTYPE_DEFAULT
from ..Name import url_to_compositeName
from ..item import WikiItem
from ..contenttypes import NonExistent as Content_NonExistent, CONTENTTYPE_NONEXISTENT
from py_tailwind_utils import H,full, bold,  shadow, bdr, bold, fz, fw, W, mr, st

#from dependency_injector import containers, providers
#from dependency_injector.wiring import Provide, inject
#from ..dependencies import Container


app = None
# @inject 
# def set_app(arg_app: Provide[Container.app_builder]):
#     global app
#     app = arg_app
#     app.add_jproute("/", wp_root, "root")
#     #jp.build_app() # <-- dependency



def show_wikiItem(wikiItem):
    """
    render the content of the wikiItem based on the contenttype 
    """
    def renderer_pagebody():
        with oj.uictx("body") as bodyCtx:
            assert  wikiItem.content.contenttype != CONTENTTYPE_NONEXISTENT
            print("show this data online = ", wikiItem.rev.data)
            oj.PD.Span(key = "panel",  text="i am a span:dryrun")
            print("chasing contenttype and data")
            print ("===> contenttype = ", wikiItem.content.contenttype)
            print ("===>  = ", wikiItem.rev.revid)

        return rendered
            
    
    return renderer_pagebody


# def show_wikiItem_(wikiItem):
#     """
#     render the content of the wikiItem based on the contenttype 

#     """
#     def renderer_pagebody(session_manager):
#         with session_manager.uictx("body") as bodyCtx:
#             _ictx=bodyCtx
#             assert  wikiItem.content.contenttype != CONTENTTYPE_NONEXISTENT
#             dummy_text = """# Hello\n##HELLOHELLO
#             """
#             with open('app_input.md', 'r') as fin: 
#                 rendered = mistletoe.markdown(fin,
#                                               mistletoe.OfjustpyRenderer,
#                                               session_manager = session_manager,
#                                               #md_view_handlers = md_view_handlers,
#                                               )
#                 # generate mditems under name panel
#                 #rendered("panel") 
#             print("show this data online = ", wikiItem.rev.data)
#             oj.Span_("panel",  text="i am a span:dryrun")
            
#             print("chasing contenttype and data")
#             print ("===> contenttype = ", wikiItem.content.contenttype)

#             print ("===>  = ", wikiItem.rev.revid)
            
            
    
#     return renderer_pagebody



def modify_wikiItem(wikiItem):
    """
    render the content of the wikiItem based on the contenttype 
    """
    def renderer_pagebody():
        with oj.uictx("body") as bodyCtx:
            title = oj.Halign(oj.PC.Span(text=wikiItem.fqcn.fullname(),
                                          twsty_tags=[fz.xl2, fw.bold]
                                          )
                               )

            divider = oj.Hr("title_divider", twsty_tags=[])
            commentbox = oj.PC.Subsubsection("Comment",
                                              oj.AC.Textarea(key="comment_input",
                                                             placeholder="enter comments for wiki item here",
                                                             twsty_tags=[W/full, H/8])
                                              )

            contentbox = oj.PC.Subsubsection("Content",
                                              oj.AC.Textarea(key="content_input",
                                                             placeholder="enter wiki item content here",
                                                             twsty_tags=[H/32]
                                                             ),
                                              twsty_tags = [mr/st/8]
                                              )


            # def on_submit_btnclick(dbref, msg):
            #     userinput = Dict()
            #     userinput.comment = _ictx.comment_input.target.value
            #     userinput.content = _ictx.content_input.target.value
            #     userinput.summary_input = _ictx.summary_input.target.value
            #     userinput.tags = _ictx.tags_input.target.value
            #     print(userinput)
            #     print ("====================================")
            #     pass
            def on_submit_btnclick(dbref, msg):
                pass
            
            #gm<-- generalmeta
            gm_title = oj.Halign(oj.PC.Span(text="General Meta",
                                              twsty_tags=[fz.lg, fw.bold]
                                              ),
                                  align="start",
                                  twsty_tags=[mr/st/8]
                                  )
            
            gm_divider = oj.Hr()
            gm_summary = oj.PC.Subsubsection("Summary",
                                            oj.AC.Textarea_(key="summary_input",
                                                            placeholder="enter summary for changes",
                                                            twsty_tags=[H/8]),
                                              twsty_tags=[mr/st/8]
                                              )
            
            gm_tags = oj.PC.Subsubsection("Tags",
                                         oj.AC.Textarea(key="tags_input",
                                                        placeholder="enter tag for content",
                                                        twsty_tags=[H/8]),
                                         twsty_tags=[mr/st/4]

                              )

            # @ojr.ReactDomino
            # def on_submit_btnclick(dbref, msg):
            #     userinput = Dict()
            #     userinput.comment = _ictx.comment_input.target.value
            #     userinput.content = _ictx.content_input.target.value
            #     userinput.summary = _ictx.summary_input.target.value
            #     userinput.tags = _ictx.tags_input.target.value
            #     userinput.wikiItem = wikiItem
            #     print ("==== userinput===")
            #     print(userinput)
            #     print ("====================================")
            #     return "/modify_wiki_item", ojr.make_opaque_dict(userinput)


            submit =oj.Halign(oj.AC.Button(key="submit",
                                           text="Create item (add to wiki)",
                                           on_click = on_submit_btnclick
                                           ),
                              twsty_tags=[mr/st/4]
                              )

            # panel is what hooks into the page template
            panel = oj.Halign(oj.PC.StackV("panel_core",
                                           childs=[title,
                                                   divider,
                                                   commentbox,
                                                   contentbox,
                                                   gm_title,
                                                   gm_divider,
                                                   gm_summary,
                                                   gm_tags,
                                                   submit
                                                   ]),
                              twsty_tags=[H/full])
            return panel
        return renderer_pagebody
    





def wp_nonexistent_wikiItem(request, fqname):
    query_str = "?itemtype=default&contenttype=text%2Fcsv%3Bcharset%3Dutf-8&template= HTTP/1.1"
    new_item_url = request.url_for("endpoint_wikiItem", item_name=fqname) + query_str

    def body_panel_builder():
        with oj.uictx("body") as bodyCtx:
            aspan = oj.PC.Span(text=f"Requested item {fqname} does not exists in wiki")
            create_link = oj.Halign(oj.AC.A(key = "create",
                              href=new_item_url,
                                      title=f"Create wiki item {fqname}",
                                      text="Create item",
                                      twsty_tags=[bold, #shadow,  shadow.sm, #TODO: fix shadow stuff
                                                  bdr.md,
                                                  bold]
                              )
                      )
            panel = oj.Halign(oj.PC.StackV(childs=[aspan, create_link]),  twsty_tags=[H/full])
        return panel
    wp_endpoint =  page_builder("wp_nonexistent_wikiItem",
                        "Non Existent wiki item",
                        body_panel_builder
                        )
    wp = wp_endpoint(request)
    print("wp= ", wp)
    print(type(wp))
    return wp
   
    
#TODO
def wp_upload_new_csv(request):
    #Assume that session context is already active
    session_id = request.session_id
    session_manager = oj.get_session_manager(session_id)
    appstate = session_manager.appstate

    with oj.sessionctx(session_manager):
        with session_manager.uictx("upload_new_csv") as upload_new_csv_ctx:
            _ictx = upload_new_csv_ctx
            #@Stuff : pass it through state-change-diagram
            def on_click(dbref, msg):
                # collect stuff from front page
                # put it on state
                # let deltas in state take care. of things
                return "/wikiItem_content", {"content ": b"ia m csv content", "comment":"this is commment", "created": "sandeep", "time": "sometime"}
            


            btn_ = oj.Button_("upload_csv_btn", text="Upload").event_handle(oj.click, on_click)

        tlc = oj.Container_("tlc", cgens=[btn_])
        wp_ = oj.WebPage_("basicpage", cgens = [tlc], title="create new csv")
        wp = wp_()
        wp.session_manager = session_manager
    return wp 


def renderhtml_wikiItem(request, wikiItem, session_manager=None):
    """
    build a webpage that shows a wikiItem on the browser. 
    Multiplex/polymorphic based on itemtype/content type 

    wikiItem is of type wikiItemTypes: [Default|NonExistent]
    wikiItem.content is of type Content: [NonExistent| CSV]
    """
    print ("render wikiItem: itemtype= ", wikiItem.itemtype)

    
    if wikiItem.itemtype == ITEMTYPE_NONEXISTENT:
        #we assume that user has right to create (see moninwiki/src/items/__init__.py:1455)
        # We should verify parents (whatever that means; and if not then create_new_item.html
        # using modify-select: wtm
        print ("show webpage for nonexists tiem")
        print ("fqcn  = ", wikiItem.fqcn)
        fullname = wikiItem.fqcn.fullname()
        print ("fullname = ", fullname)
        return wp_nonexistent_wikiItem(request, fullname)
        pass
    if wikiItem.itemtype == ITEMTYPE_DEFAULT:
        #print ("render wikiItem: content= ", wikiItem.content.contenttype)
        # return an html response for default item
        # Currently, no good way to telll if we need to upload a new csv or view an existing csv
        # using the revid  condition to determine
        print ("there is rev ", wikiItem.rev.revid)
        if wikiItem.rev.revid == None:
            # There is no content; but the contenttype is defined. 
            # render modify_item.html 
            # 
            #return wp_modify(request, )
            return page_builder("wp_modify_wikiItem",
                        "modify/create a wiki item", modify_wikiItem_(wikiItem)
                                )(request)

        if wikiItem.rev.revid is not  None:
            # this is a fully fledged filled out item : show it.
            print(" render a full fledged item ")
            wp_endpoint = page_builder("wp_show_wikiItem",
                                       "show_wikiItem",
                                       show_wikiItem(wikiItem)
                                )

            print("wp_endpoint = ", wp_endpoint)
            wp = wp_endpoint(request)
            return wp

    assert False
    
# all urls for /<itemname> will arrive here; if an item with the itemname exists -- its content
# will be rendered based on its itemtyp/contenttype; if itemname does not exists then choice
# will be given to select the itemtype/contenttype 
def endpoint_wikiItem(request, rev = CURRENT, item_name =None):
    print ("show_wikiItem invoked: with rev, itemName", rev, item_name)
    print ("query_params = ", request.query_params._dict)
    itemtype = request.query_params._dict.get('itemtype', ITEMTYPE_NONEXISTENT)
    contenttype = request.query_params._dict.get('contenttype', None)
    fqcn = url_to_compositeName(item_name)
    wikiItem = WikiItem.create(fqcn, rev_id=rev, itemtype = itemtype, contenttype=contenttype)
    return renderhtml_wikiItem(request, wikiItem)

endpoint_wikiItem.route_name = "endpoint_wikiItem"
# def modify_wikiitem(request, item_name=None):
#     """
#     if wikiitem with name = item_name; then show its various content for edititng;
#     else create the item  (including choice for content type markdown/csv/etc). 
    
#     """
#     itemtype = request.path_params['itemtype'] #do not resort to default item type;
#     contenttype = request.path_params['contenttype'] #contenttype path params is mandatory
#     item = Item.create(item_name, itemtype=itemtype, contenttype=contenttype)
#     ret = item.do_modify()
#     return ret 

#jp.CastAsEndpoint(endpoint_wikiItem, "/{rev}/{item_name}", "show_wikiItem")
#jp.CastAsEndpoint(endpoint_wikiItem, "/{item_name}", "show_wikiItem")
# app.add_jproute("/{rev}/{item_name}", endpoint_wikiItem, "endpoint_wikiItem")
# app.add_jproute("/{item_name}", endpoint_wikiItem, "endpoint_wikiItem")

# def build_app(**kwargs):
#     global app
#     app = oj.build_app(**kwargs)
#     app.add_jproute("/", wp_root, "root")
#     app.add_jproute("/{rev}/{item_name}", endpoint_wikiItem, "endpoint_wikiItem")
#     app.add_jproute("/{item_name}", endpoint_wikiItem, "endpoint_wikiItem")
    

    

# def modify_select_itemtype(fqname:CompositeName):
#     """
#     show an href to csv item creating link; but first lets create csv-item-create-page
#     """
#     # oj.Title_("Item not found, create it now")
#     # content_ = oj.Prose_("prose", "item {fqname.fullname} does not exists; Create  it now")
    
#     # oj.Subsection_("heading", "Item not found, create it now?", content_)

    
#     pass


ui_app_trmap_iter = [
    ]
app = oj.load_app()


aspan = oj.PC.Span(text="dummy text"
                   )

wp_root = oj.create_endpoint(key="wp_root",
                                 childs=[aspan],
                                 title="The root page for wiki"
                                 )
wp_root.redirect ="/Home"
oj.add_jproute("/", wp_root)
oj.add_jproute("/{rev}/{item_name}", endpoint_wikiItem)
oj.add_jproute("/{item_name}", endpoint_wikiItem)
    
# def wp_root(request):
#     """
    
#     """

#     # wp_template = oj.Mutable.WebPage(key="wp_root",
#     #                           childs = [aspan],
#     #                                  #ui_app_trmap_iter = ui_app_trmap_iter,
#     #                                  #action_module = actions,
#     #                                  title="The root page for wiki"
#     #                           )
#     # wp_endpoint = oj.create_endpoint(wp_template)
#     return wp_endpoint





