var OnDoubleClickListener =  function (config)
{
    //double click detect sourced from https://stackoverflow.com/users/1793477/sudarshan
    var max_interval = 250;
    var one_click = false;
    var timer;

    if (config && config.onDoubleClick instanceof Function)
        return function (tab)
        {
            if (one_click) {
                clearTimeout(timer);
                one_click = false;
                return config.onDoubleClick.apply(config.onDoubleClick, [tab]);
            }
            one_click = true;
            timer = setTimeout(function ()
            {
                //single click
                chrome.browserAction.setIcon({ path: "128on.png" });
                set_status(1);
                clearTimeout(timer);
                one_click = false;
            }, max_interval);
        };
    throw new Error("[InvalidArgumentException]");
};


chrome.browserAction.onClicked.addListener(new OnDoubleClickListener({
    onDoubleClick: function (tab)
    {
        chrome.browserAction.setIcon({ path: "128off.png" });
        set_status(0);
    }
}));

function set_status(new_status)
{
    const id = "1";
    const auth_key = "<AUTH_KEY1>"
    const base_url = "http://<BASE_URL>.herokuapp.com/"
    const status_url = "set_status/?new_status="

    let endpoint = base_url + status_url + new_status + "&id=" + id + "&auth_key=" + auth_key;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", endpoint, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        "Message": "None"
    }));

}

function sleep(ms)
{
    return new Promise(resolve => setTimeout(resolve, ms));
}
