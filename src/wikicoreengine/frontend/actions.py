"""

"""
from wikicoreengine.constant_keys import NAME, NAMESPACE, NAME_EXACT, NAMESPACE_DEFAULT, CURRENT, CONTENTTYPE, REVID
from wikicoreengine.Name import CompositeName

from ..data.storage_routing import storage_routing
from ..data.indexes import indexes
from ..item import WikiItem
def modify_wiki_item(appstate, arg, wp):
    """
    appctx:/modify_wiki_item
    """
    print ("in modify wiki item appstate= ", appstate)
    print ("in modify wiki item arg= ", arg)
    wikiItem = arg.wikiItem
    meta =  {'itemtype': wikiItem.itemtype,
             'contenttype': wikiItem.content.contenttype,
             'namespace': wikiItem.rev.idxitem.query['namespace'], #For now lets just keep the namespace default
             'summary': arg.summary,
             'name': [wikiItem.rev.idxitem.query['name_exact']], #for now going just with name_exact; -- there maybe others names as well -- we will see
             'tags': arg.tags,
             'comment': arg.comment,
         }
    print ("meta = {meta}")
    data = arg.content.encode("utf-8") #we should figure out the encoding business
    revid = storage_routing.store(meta, data)
    storage_routing.commit()

    #TODO: how do we know its new data? 
    content =  indexes.indexible_content(meta, data, is_new = True)
    indexes.save(wikiItem, meta, data,  storage_revid = revid)
    
    itemtype =  'default'
    contenttype =  'text/x-markdown;charset=utf-8'
    print("name_exact = ", wikiItem.rev.idxitem.query['name_exact'])
    fqcn = CompositeName(wikiItem.rev.idxitem.query['namespace'],
                         NAME_EXACT, 
                         wikiItem.rev.idxitem.query['name_exact'])

    wikiitem = WikiItem.create(fqcn, itemtype=itemtype, contenttype=contenttype)
    print (revid)
    print ("should have revid")
    print (" wikiitem  = ", wikiitem)

    pass
