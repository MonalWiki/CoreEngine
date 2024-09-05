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
from py_tailwind_utils import H,full, bold,  shadow, bdr, bold, fz, fw, W, mr, st, db, flxdir

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

    with oj.uictx("body") as bodyCtx:
        print("show this data online = ", wikiItem.rev.data)
        
        panel = oj.PD.Span(text=wikiItem.rev.data)
        return panel
    # def renderer_pagebody():
    #     with oj.uictx("body") as bodyCtx:
    #         assert  wikiItem.content.contenttype != CONTENTTYPE_NONEXISTENT
    #         print("show this data online = ", wikiItem.rev.data)
    #         oj.PD.Span(key = "panel",  text="i am a span:dryrun")
    #         print("chasing contenttype and data")
    #         print ("===> contenttype = ", wikiItem.content.contenttype)
    #         print ("===>  = ", wikiItem.rev.revid)

    #     return rendered
            
    
    # return renderer_pagebody


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


# ======================= modify_wikiItem panel ======================
# static parts
def on_input_change(dbref, msg, to_ms):
    pass

divider = oj.PC.Hr(key="title_divider", twsty_tags=[])
commentbox = oj.PC.Subsection("Comment",
                                  oj.AC.Textarea(key="comment_input",
                                                 placeholder="enter comments for wiki item here",
                                                 value="no-comments-entered",
                                                 
                                                 twsty_tags=[W/full, H/8],
                                                 on_change = on_input_change
                                                 ),
                              section_depth=8
                                  )

contentbox = oj.PC.Subsection("Content",
                                  oj.AC.Textarea(key="content_input",
                                                 placeholder="enter wiki item content here",
                                                 value="no-content-entered",
                                                 twsty_tags=[H/32],
                                                 on_change = on_input_change
                                                 ),
                              section_depth=8,
                                  twsty_tags = [mr/st/8]
                                  )

gm_title = oj.Halign(oj.PC.Span(text="General Meta",
                                  twsty_tags=[fz.lg, fw.bold]
                                  ),
                      align="start",
                      twsty_tags=[mr/st/8]
                      )

gm_divider = oj.PC.Hr()
gm_summary = oj.PC.Subsection("Summary",
                                oj.AC.Textarea(key="summary_input",
                                                placeholder="enter summary for changes",
                                               value="no summary  entered", 
                                                twsty_tags=[H/8],
                                               on_change = on_input_change,
                                               ),
                              section_depth=8,

                                  twsty_tags=[mr/st/8]
                                  )

gm_tags = oj.PC.Subsection("Tags",
                             oj.AC.Textarea(key="tags_input",
                                            placeholder="enter tag for content",
                                            value="no tags entered",
                                            on_change = on_input_change,
                                            twsty_tags=[H/8]),
                           section_depth=8,
                             twsty_tags=[mr/st/4]

                  )

submit_btn =oj.Halign(oj.AC.Button(key="submit",
                               text="Create item (add to wiki)",
                                   value=None
                               ),
                  twsty_tags=[mr/st/4]
                  )
@ojr.ReactDomino
async def on_modifyWiki_form_submit(dbref, msg, to_ms):
    print("modify form submit clicked: ", dbref.id)
    form_data = msg.page.session_manager.request.state.form_data["/form_modify_wikiItem"]
    comment_input_value = dbref.get_comp_value(msg.page, "/comment_input")
    content_input_value = dbref.get_comp_value(msg.page, "/content_input")
    summary_input_value = dbref.get_comp_value(msg.page, "/summary_input")
    tags_input_value = dbref.get_comp_value(msg.page, "/tags_input")
    wikiItem = msg.page.session_manager.request.state.current_wikiItem
    
    res = ojr.make_opaque_dict({ 'wikiItem' : wikiItem,
            'summary': summary_input_value,
            'tags' : tags_input_value,
            'content': content_input_value,
            'comment': comment_input_value
        })
    return "/modify_wiki_item",  res

modifyWiki_form = oj.AD.Form(key="form_modify_wikiItem", 
                             childs = [divider,
                                       commentbox,
                                               contentbox,
                                               gm_title,
                                               gm_divider,
                                               gm_summary,
                                               gm_tags,
                                       divider,
                                       submit_btn
                                       

                             ],
                             twsty_tags=[db.f, flxdir.col],
                             on_submit = on_modifyWiki_form_submit
                             )
        

def panel_modify_wikiItem(wikiItem):
    """
    render the content of the wikiItem based on the contenttype 
    """
    with oj.uictx("body") as bodyCtx:
        title = oj.Halign(oj.PC.Span(text=wikiItem.fqcn.fullname(),
                                      twsty_tags=[fz.xl2, fw.bold]
                                      )
                           )
        
        # panel is what hooks into the page template
        panel = oj.Halign(oj.PC.StackV(key="panel_core",
                                       childs=[title,
                                               modifyWiki_form
                                               ]),
                          twsty_tags=[H/full])
        return panel

    





def wp_nonexistent_wikiItem(request, fqname):
    query_str = "?itemtype=default&contenttype=text%2Fcsv%3Bcharset%3Dutf-8&template= HTTP/1.1"
    new_item_url = str(request.url_for("endpoint_wikiItem", item_name=fqname)) + query_str

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


    with oj.PageBuilderCtx(page_builder):
        wp_endpoint = oj.create_endpoint("wp_nonexistent_wikiItem",
                                         [panel],
                                         title = "Non Existent wiki item",
                                         )

    wp = wp_endpoint(request)

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

        # fix cgens to childs 
        assert False            
        tlc = oj.Container_("tlc", cgens=[btn_])
        wp_ = oj.WebPage_("basicpage", cgens = [tlc], title="create new csv")
        wp = wp_()
        wp.session_manager = session_manager
    return wp 


def renderhtml_wikiItem(request, wikiItem):
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
            ui_app_trmap = [("/modify_wiki_item", "/modify_wiki_item", None
                             )

                ]
            
            def post_init(wp, session_manager=None):
                assert "session_manager" != None
                request = wp.session_manager.request
                request.state.form_data["/form_modify_wikiItem"] = {}
                request.state.current_wikiItem = wikiItem
                pass
            
            with oj.PageBuilderCtx(page_builder):
                wp_endpoint = ojr.create_endpoint("wp_modify_wikiItem",
                                                 [panel_modify_wikiItem(wikiItem)],
                                                 title="modify/create a wiki item",
                                                 post_init = post_init,
                                                  ui_app_trmap_iter = ui_app_trmap,
                                                  action_module = actions,

                                )
            return wp_endpoint(request)
            # return page_builder("wp_modify_wikiItem",
            #                     "modify/create a wiki item", modify_wikiItem_(wikiItem)
            #                     )(request)

        if wikiItem.rev.revid is not  None:
            # this is a fully fledged filled out item : show it.

            ui_app_trmap = [

                ]
            
            with oj.PageBuilderCtx(page_builder):
                wp_endpoint = ojr.create_endpoint("wp_show_wikiItem",
                                                 [show_wikiItem(wikiItem)],
                                                  title="show wikiitem",
                                                  ui_app_trmap_iter = ui_app_trmap,
                                                  action_module = actions,

                                )
            return wp_endpoint(request)

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

    try:
        wikiItem = WikiItem.create(fqcn, rev_id=rev, itemtype = itemtype, contenttype=contenttype)
    except Exception as e:
        print("Failed e ", e)
        raise e

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





