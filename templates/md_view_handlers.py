import ofjustpy as oj
#this is the default list item viwer
from py_tailwind_utils import *
from jsonpath_ng import jsonpath, parse

session_manager = None

def list_item(cgens, key_cursor):
    return oj.StackV_("blahblah", cgens=[])

def gridify(mditem_data, key_cursor):
    print ("in gridify ", mditem_data)
    return oj.StackG_("mygrid", num_cols=3, cgens=mditem_data['list'])


def list_item_view_formatter(mditem_data, key_cursor):
    # print ("==========in list_item_view_formatter=================")
    #print (mditem_data)
    # opts = jsbeautifier.default_options()
    # res = jsbeautifier.beautify(json.dumps(mditem_data), opts)

    # we expect only one para for this metadata
    assert 'list_item' in mditem_data
    assert len(mditem_data['list_item']) == 1
    print ("in list_item_view_formatter", mditem_data)
    
    para = mditem_data['list_item'][0]['para']
    return oj.Span_("some", text="hello")
    #we expect only one ahref per para
    # assert len(para[0]) == 1
    # href_entry = para[0]['ahref']
    # return oj.A_(Path(href_entry.target).stem,
    #              href=href_entry.target,
    #              title=href_entry.title,
    #              text=href_entry.desc
    #              )


#this is the default list item viwer
def para_as_span_viewer(mditem_data, key_cursor):
    """
    strip para and graph the rawText to define the span
    """

    print (mditem_data)
    jsonpath_expr = parse('$.list_item[0].para[0].rawText')
    span_text = [_.value for _ in jsonpath_expr.find(mditem_data)][0]
    print ('span_text = ', span_text)
    return oj.Span_("aspan", text =span_text)

#this is the default list item viwer
def href_image_viewer(mditem_data, key_cursor):
    #print ("in href_image_viewer  = ", mditem_data)
    #/list_item/0/para/rawText
    jsonpath_expr = parse('$.list_item[0].para[0].ahref')
    _d  = [_.value for _ in jsonpath_expr.find(mditem_data)][0]
    jsonpath_expr = parse('$.list_item[0].para[2].img')
    _i = [_.value for _ in jsonpath_expr.find(mditem_data)][0]
    print (_i)
    with session_manager.uictx(f"item_{key_cursor}") as _ictx:
        href = oj.A_("ahref", text= _d.desc, title = _d.title, href=_d.target)
        img = oj.Img_("img", src =_i.src, title = _d.title, alt=_d.desc, pcp=[of.cn]) # 
        return oj.StackV_("box", cgens=[href, img])


    
