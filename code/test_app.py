


def test_success_request_page_route(app, client):
    res = client.get('/')
    assert res.status_code == 200


def test_render_html_page_route(app, client):
    res = client.get('/')
    expected = '<h2 class="text-center">Flask Example CI/CD</h2>'
    assert expected in res.get_data(as_text=True)